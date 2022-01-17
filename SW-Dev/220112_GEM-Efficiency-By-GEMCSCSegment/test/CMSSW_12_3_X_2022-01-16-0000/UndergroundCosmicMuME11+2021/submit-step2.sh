#!/bin/sh
source setup.sh

PREV_CFG=step1_GEN_SIM.py
CFG=step2_DIGI_L1_DIGI2RAW_HLT.py

PREV_STEP=${PREV_CFG/".py"/""}
STEP=${CFG/".py"/""}

JOB_BATCH_NAME=${JOB_BATCH_NAME_PREFIX}__${STEP}
INPUT_DIR=${OUTPUT_ROOT}/${PREV_STEP}
OUTPUT_DIR=${OUTPUT_ROOT}/${STEP}
LOG_DIR=./logs/${STEP}

check_log_dir ${LOG_DIR}

COMMAND="gem-dqm-submit.py -i ${INPUT_DIR} -o ${OUTPUT_DIR} -l ${LOG_DIR} -b ${JOB_BATCH_NAME} ${CFG}"
echo ${COMMAND}
eval ${COMMAND}
