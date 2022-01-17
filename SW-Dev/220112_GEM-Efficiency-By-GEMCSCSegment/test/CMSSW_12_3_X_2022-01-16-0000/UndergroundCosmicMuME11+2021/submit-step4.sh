#!/bin/sh
PROJECT=220101_GEM-Efficiency-By-GEMCSCSegment
TAG=CMSSW_12_3_0_pre2
SAMPLE="UndergroundCosmicMuME11+2021"

PREV_CFG=step3_RAW2DIGI_L1Reco_RECO.py
PREV_STEP=${PREV_CFG/".py"/""}

CFG=step4_DQM.py
STEP=${CFG/".py"/""}

JOB_BATCH_NAME=${PROJECT}__${TAG}__${SAMPLE}__${STEP}
SAMPLE_DIR=/xrootd/store/user/seyang/GEM/${PROJECT}/${TAG}/${SAMPLE}
INPUT_DIR=${SAMPLE_DIR}/${PREV_STEP}
OUTPUT_DIR=${SAMPLE_DIR}/${STEP}
LOG_DIR=./logs/${STEP}

if [ -d ${LOG_DIR} ]
then
    rm -f ${LOG_DIR}/*.log ${LOG_DIR}/*.out ${LOG_DIR}/*.err
else
    mkdir -vp ${LOG_DIR}
fi

gem-dqm-submit.py \
    -i ${INPUT_DIR} \
    -o ${OUTPUT_DIR} \
    -l ${LOG_DIR} \
    -b ${JOB_BATCH_NAME} \
    ${CFG}
