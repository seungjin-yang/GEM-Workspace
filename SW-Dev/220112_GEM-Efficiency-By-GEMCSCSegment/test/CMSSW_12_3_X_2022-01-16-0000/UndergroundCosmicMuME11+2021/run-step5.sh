#!/usr/bin/env sh
CFG=step5_HARVESTING.py
INPUT_FILE=filelist-step4_DQM.txt
FILE_PREPEND=file:

STEP=${CFG/".py"/""}
LOG_FILE=./logs/${STEP}.txt

cmsRun ${CFG} inputFiles_load=${INPUT_FILE} filePrepend=${FILE_PREPEND} > ${LOG_FILE} 2>&1
tail -f ${LOG_FILE}
