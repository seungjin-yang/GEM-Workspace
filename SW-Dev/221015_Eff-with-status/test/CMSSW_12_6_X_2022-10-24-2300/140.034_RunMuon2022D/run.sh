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
output_file=${3}
cmssw_version=${4}
author=${5}
branch=${6}

checkvar config_file
checkvar input_file
checkvar author
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
if [[ ! -z ${author} && ! -z ${branch} ]]; then
    echo "running 'git-cms-merge-topic ${author}:${branch}'"
    git-cms-merge-topic ${author}:${branch}
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
    outputFile=${output_file}

###############################################################################
# report
###############################################################################
stat ${output_file}

echo "end: $(date)"
