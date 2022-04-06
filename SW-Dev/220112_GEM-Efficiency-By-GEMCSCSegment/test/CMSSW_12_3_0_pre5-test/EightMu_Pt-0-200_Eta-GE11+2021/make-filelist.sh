#!/usr/bin/env sh
DATA_DIR=${1}
if [ -z ${DATA_DIR} ]; then
    echo "DATA_DIR"
    exit 1
fi


OUTPUT_FILE=filelist-$(basename ${DATA_DIR}).txt

find ${DATA_DIR} -name "*.root" | sort > ${OUTPUT_FILE}

wc -l ${OUTPUT_FILE}
