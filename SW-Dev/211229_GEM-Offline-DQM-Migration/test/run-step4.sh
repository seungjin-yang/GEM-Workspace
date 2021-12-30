#!/usr/bin/env sh
CFG=step4_DQM.py
INPUT_FILE_LIST=./filelist-2021-ZMM-step3.txt
FILE_PREPEND=root://eoscms.cern.ch//eos/cms/
OUTPUT_FILE=./step4.root

NUM_THREADS=$(wc -l ${INPUT_FILE_LIST} | awk '{ print $1 }')

COMMAND="cmsRun -n ${NUM_THREADS} ${CFG} inputFiles_load=${INPUT_FILE_LIST} filePrepend=${FILE_PREPEND} outputFile=${OUTPUT_FILE}"
echo ${COMMAND}
eval ${COMMAND}
