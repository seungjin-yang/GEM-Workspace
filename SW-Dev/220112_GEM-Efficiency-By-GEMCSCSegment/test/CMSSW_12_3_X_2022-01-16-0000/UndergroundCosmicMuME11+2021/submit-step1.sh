#!/bin/sh
source setup.sh

CFG=step1_GEN_SIM.py
NUM_JOBS=500

STEP=${CFG/".py"/""}
JOB_BATCH_NAME=${JOB_BATCH_NAME_PREFIX}__${STEP}
OUTPUT_DIR=${OUTPUT_ROOT}/${STEP}
LOG_DIR=./logs/${STEP}

check_log_dir ${LOG_DIR}

COMMAND="gem-dqm-submit.py -o ${OUTPUT_DIR} -l ${LOG_DIR} -n ${NUM_JOBS} -b ${JOB_BATCH_NAME} ${CFG}"
echo ${COMMAND}
eval ${COMMAND}
