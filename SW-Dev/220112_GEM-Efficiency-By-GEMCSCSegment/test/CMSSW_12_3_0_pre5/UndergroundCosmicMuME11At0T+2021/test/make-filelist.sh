#!/usr/bin/env sh
INPUT_DIR=${1}
OUTPUT_FILE=${2:-""}

if [ -z ${INPUT_DIR} ]; then
    echo "the following arguments are required: INPUT_DIR"
    exit
fi

if [ -z ${OUTPUT_FILE} ]; then
    OUTPUT_FILE=./filelist-$(basename ${INPUT_DIR}).txt
fi

find ${INPUT_DIR} -name "*.root" | sort > ${OUTPUT_FILE}
