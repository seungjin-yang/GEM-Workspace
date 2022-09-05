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
config_file=${1}
input_file=${2}
file_prepend=${3}
output_file=${4}
cmssw_version=${5}
branch=${6}

checkvar config_file
checkvar input_file
checkvar file_prepend
checkvar output_file
checkvar cmssw_version
checkvar branch

###############################################################################
# setup
###############################################################################
source /cvmfs/cms.cern.ch/cmsset_default.sh
cmsrel ${cmssw_version}
cd ${cmssw_version}/src
eval `scramv1 runtime -sh`
if [ ! -z ${branch} ]; then
    git-cms-merge-topic ${branch}
fi
scram b
cd -

checkvar SCRAM_ARCH
checkvar CMSSW_VERSION
checkvar CMSSW_BASE

###############################################################################
# run
###############################################################################
cmsRun ${config_file} \
    inputFiles=${input_file} \
    filePrepend=${file_prepend} \
    outputFile=${output_file}

###############################################################################
# report
###############################################################################
stat ${output_file}

echo "end: $(date)"
