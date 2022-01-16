#!/usr/bin/env sh
CFG=./step3_RAW2DIGI_L1Reco_RECO.py
INPUT_FILE_LIST=./filelist-2021-ZMM-step2.txt
FILE_PREPEND=root://eoscms.cern.ch//eos/cms/
MAX_EVENTS=1000
OUTPUT_FILE=./step3.root

COMMAND="cmsRun ${CFG} inputFiles_load=${INPUT_FILE_LIST} filePrepend=${FILE_PREPEND} maxEvents=${MAX_EVENTS} outputFile=${OUTPUT_FILE}"
echo ${COMMAND}
eval ${COMMAND}
