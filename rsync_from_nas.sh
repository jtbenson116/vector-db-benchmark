#!/bin/bash

set -e
set -x

USER=jacob
SOURCEDIR="/mnt/nas2/$USER/vdbenchmark_results/"
SOURCE="$USER@192.168.99.40:$SOURCEDIR"
mkdir -p ./results
rsync -azvd0 --no-owner --no-group --no-perms "$SOURCE" ./results/
