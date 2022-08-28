#!/usr/bin/env bash
###############################################################################
# tools
###############################################################################
function checkvar() {
    VAR=${1}
    echo "${VAR}=${!VAR}"
}

###############################################################################
# print info
###############################################################################
echo "start: $(date)"
echo "hostname: $(hostname)"
echo "pwd: $(pwd)"
ls -lha ./

###############################################################################
# arguments
###############################################################################
input_file=${1}
output_file=${2}

checkvar input_file
checkvar output_file

###############################################################################
# setup
###############################################################################
CMSSW_VERSION=CMSSW_12_5_0_pre4
source /cvmfs/cms.cern.ch/cmsset_default.sh
cmsrel ${CMSSW_VERSION}
cd ${CMSSW_VERSION}/src
eval `scramv1 runtime -sh`
git-cms-merge-topic slowmoyang:ge21-me21-seg-reco__from-CMSSW_12_5_0_pre4
scram b
cd -

checkvar SCRAM_ARCH
checkvar CMSSW_VERSION
checkvar CMSSW_BASE

###############################################################################
# run
###############################################################################
cfg_file=step2_RAW2DIGI_L1Reco_RECO_GEMCSCSegment.py
file_prepend="root://eoscms.cern.ch//eos/cms"

cmsRun ${cfg_file} \
    inputFiles=${input_file} \
    filePrepend=${file_prepend} \
    outputFile=${output_file}

###############################################################################
# report
###############################################################################
stat ${output_file}

echo "end: $(date)"
