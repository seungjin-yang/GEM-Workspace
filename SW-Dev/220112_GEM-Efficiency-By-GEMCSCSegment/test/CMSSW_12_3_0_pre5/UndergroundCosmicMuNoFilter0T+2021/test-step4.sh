#!/usr/bin/env sh
source setup.sh
CFG=step4_DQM.py
INPUT_FILE=file:./output/step3.root
LOG_FILE="./logs/test-step4.txt"

echo "CMSSW_BASE=${CMSSW_BASE}"

cmsRun -n 5 ${CFG} inputFiles=${INPUT_FILE} > ${LOG_FILE} 2>&1 &

tail -f ${LOG_FILE}
