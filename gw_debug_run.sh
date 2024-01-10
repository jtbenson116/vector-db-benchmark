#!/bin/bash

# Set this to a valid dataset id
export VDBB_FVS_DATASETID="cc7775b6-c94a-4d19-9c22-ec6474184712"

#unset VDBB_FVS_DATASETID

python3 run.py --engines gsi-768-clusters --datasets deep-image-96-angular

