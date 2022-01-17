#!/bin/sh
source /cvmfs/cms.cern.ch/cmsset_default.sh
cd ../../../CMSSW_12_3_X_2022-01-16-0000/src/
eval `scramv1 runtime -sh`
cd -

PROJECT=220112_GEM-Efficiency-By-GEMCSCSegment
SAMPLE=UndergroundCosmicMuME11+2021

if [[ $(hostname) == "gate" ]]; then
    DATA_DIR=/store/user/seyang/GEM/
elif [[ $(hostname) == "ui20.sdfarm.kr" ]]; then
    DATA_DIR=/xrootd/store/user/seyang/GEM/
else
    echo "unkown hostname: $(hostname)"
    exit 1
fi

OUTPUT_ROOT=${DATA_DIR}/${PROJECT}/${CMSSW_VERSION}/${SAMPLE}
JOB_BATCH_NAME_PREFIX=${PROJECT}__${CMSSW_VERSION}__${SAMPLE}

if [ ! -d ${OUTPUT_ROOT} ]
then

    if [[ $(hostname) == "gate" ]]; then
        mkdir -vp ${OUTPUT_ROOT}
    elif [[ $(hostname) == "ui20.sdfarm.kr" ]]; then
        mkdir -vp /xrootd_user/slowmoyang/xrootd2/GEM/${PROJECT}/${CMSSW_VERSION}/${SAMPLE}
    else
        echo "unkown hostname: $(hostname)"
        exit 1
    fi

fi

## helper functions
function print_var() {
    VAR=${1}
    echo "${VAR}=${!VAR}"
}

function check_log_dir() {
    LOG_DIR=${1}
    if [ -d ${LOG_DIR} ]; then
        rm -f ${LOG_DIR}/*.log ${LOG_DIR}/*.out ${LOG_DIR}/*.err
    else
        mkdir -vp ${LOG_DIR}
    fi
}

##########
print_var CMSSW_BASE
print_var CMSSW_VERSION
print_var OUTPUT_ROOT
print_var JOB_BATCH_NAME_PREFIX
