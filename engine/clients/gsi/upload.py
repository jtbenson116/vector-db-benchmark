from typing import List, Optional
from npy_append_array import NpyAppendArray
import numpy as np
import h5py
import os, time
from swagger_client.models import *
from engine.base_client.upload import BaseUploader
from engine.clients.gsi.client import GSIClient
from engine.clients.gsi.config import GSI_DEFAULT_DATA_PATH

DEBUG = False

class GSIUploader(BaseUploader):
    client = None
    global skip
    skip = True

    @classmethod
    def init_client(cls, host, distance, connection_params: dict, upload_params: dict):
        cls.client = GSIClient(host, connection_params)
        cls.upload_params = upload_params
        if DEBUG: print("GSIUploader: init_client: upload params:", upload_params)
        cls.connection_params = connection_params
        cls.data = None

       
        # check for an existing fvs datasetid to use (for debugging)
        # Note that we are assuming its loaded and focused
        use_datasetid = os.getenv("VDBB_FVS_DATASETID")
        if use_datasetid:
            print("Warning: GSIUploader: init_client: Using FVS Dataset ID=", use_datasetid )
            return

        # TODO: do better!
        if os.path.exists(GSI_DEFAULT_DATA_PATH):
            os.remove(GSI_DEFAULT_DATA_PATH)

        # get dataset shape
        path = os.path.join(os.path.abspath("./datasets"), os.getenv("DATA_PATH"))
        if os.getenv("dataset") == "laion-small-clip":
            path = os.path.join(path, "vectors.npy")
            tmp = np.load(path)
            cls.shape = tmp.shape[0]
            print("shape:", cls.shape)
            return
        else:
            file = h5py.File(path)
            cls.shape = file['train'].shape[0]
            
        if skip:
            print(f"saving {path} to {GSI_DEFAULT_DATA_PATH}")
            np.save(GSI_DEFAULT_DATA_PATH, file['train'][:])
            cls.fvs_upload()

    @classmethod
    def upload_batch(cls, ids: List[int], vectors: List[list], metadata: Optional[List[dict]]):
        if skip:
            if DEBUG: print("GSIUploader: upload_batch: skip", len(vectors))
            return
        data = np.array(vectors)
        if DEBUG: print("GSIUploader: upload_batch: vectors shape", data.shape)
        with NpyAppendArray(GSI_DEFAULT_DATA_PATH) as npaa:
            npaa.append(data)
            if npaa.shape[0] >= cls.shape:
                npaa.close()
                print("done batching, shape", cls.shape)
                cls.fvs_upload()
            npaa.close()

    @classmethod
    def fvs_upload(cls):

        # check for an existing fvs datasetid to use (for debugging)
        use_datasetid = os.getenv("VDBB_FVS_DATASETID")
        if use_datasetid:
            print("Warning: GSIUploader: fvs_upload: Using FVS Dataset ID=", use_datasetid )
            cls.client.dataset_ids.append(dataset_id)
            print("GSIUploader: fvs_upload: cls.client.dataset_ids=", cls.client.dataset_ids)
            return

        nbits = cls.upload_params["nbits"] or 768
        search_type = cls.upload_params["searchType"] or "flat"
        top = cls.upload_params["top"] or 10
        m, efc = None, None
        if search_type == "hnsw":
            m = cls.upload_params["m"] or None
            efc = cls.upload_params["efConstruction"] or None

        if DEBUG: print("GSIUploader: fvs upload: params=", nbits, search_type, top, m, efc)

        # convert dataset to float32...
        data = np.load(GSI_DEFAULT_DATA_PATH)
        if DEBUG: print("GSIUploader: fvs_upload: dataset before", data.shape, data.dtype, data[0][0])

        if not isinstance(np.float32, type(data[0][0])):
            data = np.float32(data)
        if os.path.exists(GSI_DEFAULT_DATA_PATH):
            os.remove(GSI_DEFAULT_DATA_PATH)
        np.save(GSI_DEFAULT_DATA_PATH, data)
        data = np.load(GSI_DEFAULT_DATA_PATH)
        
        if DEBUG: print("GSIUploader: fvs_upload: dataset after", data.shape, data.dtype, data[0][0])

        # import dataset
        if DEBUG: print("GSIUploader: fvs_upload: dataset import parms", search_type, GSI_DEFAULT_DATA_PATH, nbits, m, efc)
        response = cls.client.datasets_apis.controllers_dataset_controller_import_dataset(
            ImportDatasetRequest(records=GSI_DEFAULT_DATA_PATH, search_type=search_type, train_ind=True,\
                                 nbits=nbits, dataset_name="QdrantBench", m_number_of_edges=m, ef_construction=efc),
            cls.client.allocation_id
        )
        if DEBUG: print("GSIUploader: fvs_upload: got datasetid=", response.dataset_id)
        dataset_id = response.dataset_id
        cls.client.dataset_ids.append(dataset_id)

        # train status
        train_status = cls.client.datasets_apis.controllers_dataset_controller_get_dataset_status(
                dataset_id=dataset_id, allocation_token=cls.client.allocation_id
            ).dataset_status
        if DEBUG: print("GSUploader: fvs_upload: training, status currently:", train_status)
        while train_status != "completed":
            train_status = cls.client.datasets_apis.controllers_dataset_controller_get_dataset_status(
                dataset_id=dataset_id, allocation_token=cls.client.allocation_id
            ).dataset_status
            time.sleep(1)

        # load dataset
        if DEBUG: print('GSIUploader: fvs_upload: done training, loading dataset...', train_status)

        load_status = cls.client.datasets_apis.controllers_dataset_controller_load_dataset(
                LoadDatasetRequest(allocation_id=cls.client.allocation_id, dataset_id=dataset_id, topk=top),
                allocation_token=cls.client.allocation_id
            ).status
        while load_status != "ok":
            load_status = cls.client.datasets_apis.controllers_dataset_controller_load_dataset(
                LoadDatasetRequest(allocation_id=cls.client.allocation_id, dataset_id=dataset_id, topk=top),
                allocation_token=cls.client.allocation_id
            ).status
        if DEBUG: print("GSIUploader: fvs_upload: load status", load_status)

        # set dataset in focus
        if DEBUG: print('GSIUploader: fvs_upload: focus dataset')
        cls.client.datasets_apis.controllers_dataset_controller_focus_dataset(
            FocusDatasetRequest(cls.client.allocation_id, dataset_id),
            cls.client.allocation_id
        )

