#!/bin/sh
source setup.sh
CFG=step4_DQM.py

STEP=$(get_step ${CFG})
JOB_BATCH_NAME=${JOB_BATCH_NAME_PREFIX}__${STEP}
INPUT_DIR=/store/user/seyang/GEM/220118_Update-GEMEfficiencyAnalyzer/CMSSW_12_3_0_pre5/UndergroundCosmicMuME11At0T+2021/step3_RAW2DIGI_L1Reco_RECO_RECOSIM
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
