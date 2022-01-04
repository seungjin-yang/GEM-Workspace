#!/usr/bin/env sh
CFG=runGEMCSCSegmentAnalyzer_cfg.py
INPUT_FILE=./step3_numEvent1000.root
FILE_PREPEND=file:
LOG_FILE="analysis.txt"

COMMAND="cmsRun ${CFG} inputFiles=${INPUT_FILE} filePrepend=${FILE_PREPEND}"
echo ${COMMAND}
eval ${COMMAND} > ${LOG_FILE} 2>&1 &
