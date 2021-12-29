#!/usr/bin/env sh
CFG=runGEMCSCSegmentAnalyzer_cfg.py
INPUT_FILE=./step3_numEvent1000.root
FILE_PREPEND=file:

COMMAND="cmsRun ${CFG} inputFiles=${INPUT_FILE} filePrepend=${FILE_PREPEND}"
echo ${COMMAND}
eval ${COMMAND}
