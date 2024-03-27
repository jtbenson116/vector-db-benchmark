#!/bin/bash

set -e
set -x

USER=gwilliams
TARGETDIR="/mnt/nas2/jacob/vdbenchmark_results/last_validation_3-25-2024_results/"
TARGET="$USER@192.168.99.40:$TARGETDIR"
rsync -azvd0  ./results/ "$TARGET"


