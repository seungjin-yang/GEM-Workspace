#!/bin/sh
source setup.sh
PREV_CFG=step3_RAW2DIGI_L1Reco_RECO_RECOSIM.py
CFG=step4_DQM.py

PREV_STEP=$(get_step ${PREV_CFG})
STEP=$(get_step ${CFG})

JOB_BATCH_NAME=${JOB_BATCH_NAME_PREFIX}__${STEP}
if [ -z ${INPUT_DIR} ]; then
    INPUT_DIR=${OUTPUT_ROOT}/${PREV_STEP}
fi
if [ -z ${OUTPUT_DIR} ]; then
    OUTPUT_DIR=${OUTPUT_ROOT}/${STEP}
fi
LOG_DIR=./logs/${STEP}

# check_output_root # FIXME
check_log_dir ${LOG_DIR}

gem-dqm-submit.py \
    -i ${INPUT_DIR} \
    -o ${OUTPUT_DIR} \
    -l ${LOG_DIR} \
    -b ${JOB_BATCH_NAME} \
    ${CFG}
