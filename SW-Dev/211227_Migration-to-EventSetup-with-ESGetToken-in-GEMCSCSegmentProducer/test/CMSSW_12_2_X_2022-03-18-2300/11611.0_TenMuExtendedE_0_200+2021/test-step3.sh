#!/usr/bin/env sh
CFG_FILE=./step3_RAW2DIGI_L1Reco_RECO.py

NAME=$(basename ${CFG_FILE})
NAME=${NAME/".py"/""}

LOG_FILE=./logs/test-${NAME}.log

NUM_THREADS=10

cmsRun -n ${NUM_THREADS} ${CFG_FILE} > ${LOG_FILE} 2>&1 &
tail -f ${LOG_FILE}
