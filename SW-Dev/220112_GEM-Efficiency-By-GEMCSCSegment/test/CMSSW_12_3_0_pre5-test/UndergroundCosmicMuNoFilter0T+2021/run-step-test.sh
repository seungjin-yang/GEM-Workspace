#!/usr/bin/env sh
source setup.sh

CFG=step5_HARVESTING.py
INPUT_FILE_LIST=filelist-step4_DQM_gemEffByGEMCSCSegmentSource_test.txt
LOG_FILE="./logs/step5_test.txt"

cmsRun ${CFG} inputFiles_load=${INPUT_FILE_LIST} filePrepend=file: > ${LOG_FILE} 2>&1 &

tail -f ${LOG_FILE}
