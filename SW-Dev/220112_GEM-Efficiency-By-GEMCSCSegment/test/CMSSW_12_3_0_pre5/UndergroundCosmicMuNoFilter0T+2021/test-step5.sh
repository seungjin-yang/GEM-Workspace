#!/usr/bin/env sh
source setup.sh

CFG=step5_HARVESTING.py
INPUT_FILE=file:./output/step4.root
LOG_FILE="./logs/test-step5.txt"

echo "CMSSW_BASE=${CMSSW_BASE}"

cmsRun ${CFG} inputFiles=${INPUT_FILE} > ${LOG_FILE} 2>&1 &

tail -f ${LOG_FILE}
