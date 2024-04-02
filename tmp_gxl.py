import hnswlib
import h5py
import os
from engine.clients.hnswlib_bench.GXL_helpers import convert_np_to_fbin
from subprocess import run

f = h5py.File("./datasets/deep-image-96-angular/deep-image-96-angular.hdf5", "r")
test = f['test'][:]
out = "/home/public/GXL_2.0/tmp/tmpDB.bin"
if not os.path.exists(out):
    convert_np_to_fbin(f["train"][:], out)
f.close()

run("./tmp_gxl.sh", shell=True)

index = hnswlib.Index(space="cosine", dim=96)
index.load_index("/home/public/GXL_2.0/tmp/deep1B_9m_ef_128_M_32_gxl.bin")

index.set_ef(64)
print("searching using ef: 64")
for i in range(len(test)):
    try:
        inds, dists = index.knn_query(test[i], k=100)
    except Exception as e:
        print(e)
        print(f'error on query no.{i}')

index.set_ef(128)
print("searching using ef: 128")
for i in range(len(test)):
    try:
        inds, dists = index.knn_query(test[i], k=100)
    except Exception as e:
        print(e)
        print(f'error on query no.{i}')

index.set_ef(256)
print("searching using ef: 256")
for i in range(len(test)):
    try:
        inds, dists = index.knn_query(test[i], k=100)
    except Exception as e:
        print(e)
        print(f'error on query no.{i}')

index.set_ef(512)
print("searching using ef: 512")
for i in range(len(test)):
    try:
        inds, dists = index.knn_query(test[i], k=100)
    except Exception as e:
        print(e)
        print(f'error on query no.{i}')