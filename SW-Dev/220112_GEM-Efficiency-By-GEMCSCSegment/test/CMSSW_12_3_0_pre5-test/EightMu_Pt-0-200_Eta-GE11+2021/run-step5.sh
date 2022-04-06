#!/usr/bin/env sh
source setup.sh

CFG=step5_HARVESTING.py
LOG_FILE="./logs/step5.txt"

INPUT_FILE_LIST=filelist-step4_GEMEffByGEMCSCSegmentSource.txt
FILE_PREPEND=file:

cmsRun ${CFG} inputFiles_load=${INPUT_FILE_LIST} filePrepend=${FILE_PREPEND} > ${LOG_FILE} 2>&1 &

tail -f ${LOG_FILE}
