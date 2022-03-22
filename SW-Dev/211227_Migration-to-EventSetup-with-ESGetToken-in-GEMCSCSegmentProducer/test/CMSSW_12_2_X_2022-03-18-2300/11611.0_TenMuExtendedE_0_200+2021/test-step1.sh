#!/usr/bin/env sh
CFG_FILE=./step1_GEN_SIM.py

NAME=$(basename ${CFG_FILE})
NAME=${NAME/".py"/""}

LOG_FILE=./logs/test-${NAME}.log

cmsRun ${CFG_FILE} > ${LOG_FILE} 2>&1 &
tail -f ${LOG_FILE}
