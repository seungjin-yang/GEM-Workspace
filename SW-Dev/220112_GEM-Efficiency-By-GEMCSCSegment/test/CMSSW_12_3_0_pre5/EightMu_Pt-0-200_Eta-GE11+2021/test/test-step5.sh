#!/usr/bin/env sh
CFG=step5_HARVESTING.py
LOG_FILE="./logs/step5.txt"

INPUT_FILE=file:step4.root
cmsRun ${CFG} inputFiles=${INPUT_FILE} > ${LOG_FILE} 2>&1 &

tail -f ${LOG_FILE}
