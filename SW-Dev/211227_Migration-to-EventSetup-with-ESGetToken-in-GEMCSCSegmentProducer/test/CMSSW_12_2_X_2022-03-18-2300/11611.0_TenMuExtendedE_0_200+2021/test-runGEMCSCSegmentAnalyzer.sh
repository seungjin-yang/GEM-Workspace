#!/usr/bin/env sh
CFG_FILE=runGEMCSCSegmentAnalyzer_cfg.py
INPUT_FILE=step3.root
FILE_PREPEND=file:

NAME=$(basename ${CFG_FILE})
NAME=${NAME/".py"/""}
LOG_FILE=./logs/test-${NAME}.log

cmsRun ${CFG_FILE} inputFiles=${INPUT_FILE} filePrepend=${FILE_PREPEND} > ${LOG_FILE} 2>&1 &
tail -f ${LOG_FILE}
