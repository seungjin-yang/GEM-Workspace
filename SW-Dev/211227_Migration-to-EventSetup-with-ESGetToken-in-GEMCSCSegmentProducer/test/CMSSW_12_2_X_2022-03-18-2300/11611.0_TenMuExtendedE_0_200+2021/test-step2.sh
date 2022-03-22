#!/usr/bin/env sh
CFG_FILE=./step2_DIGI_L1_DIGI2RAW_HLT.py

NAME=$(basename ${CFG_FILE})
NAME=${NAME/".py"/""}

LOG_FILE=./logs/test-${NAME}.log

NUM_THREADS=2

cmsRun -n ${NUM_THREADS} ${CFG_FILE} > ${LOG_FILE} 2>&1 &
tail -f ${LOG_FILE}
