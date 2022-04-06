#!/usr/bin/env sh
CFG=step3_RAW2DIGI_L1Reco_RECO_RECOSIM.py
INPUT_FILE=file:step2.root
LOG_FILE="./logs/test-step3.txt"

echo "CMSSW_BASE=${CMSSW_BASE}"

cmsRun -n 10 ${CFG} inputFiles=${INPUT_FILE} > ${LOG_FILE} 2>&1 &

tail -f ${LOG_FILE}
