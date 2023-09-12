import swagger_client
from swagger_client.models import *
from engine.clients.gsi.config import GSI_DEFAULT_ALLOC, GSI_DEFAULT_PORT, GSI_DEFAULT_VERSION

class GSIClient:
    def __init__(self, host, connection_params):
        config = swagger_client.Configuration()
        config.verify_ssl = False
        config.host = f"http://{host}:{GSI_DEFAULT_PORT}/{GSI_DEFAULT_VERSION}"
        api_config = swagger_client.ApiClient(config)
        api_config.default_headers["allocationToken"] = GSI_DEFAULT_ALLOC    
        self.allocation_id = GSI_DEFAULT_ALLOC

        self.datasets_apis = swagger_client.DatasetsApi(api_config)
        self.search_apis = swagger_client.SearchApi(api_config)
        self.utilities_apis = swagger_client.UtilitiesApi(api_config)

        self.dataset_ids = []