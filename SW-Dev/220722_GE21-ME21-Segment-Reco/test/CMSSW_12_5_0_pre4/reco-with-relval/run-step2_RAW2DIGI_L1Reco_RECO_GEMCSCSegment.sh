#!/usr/bin/env bash
echo "hostname: $(hostname)"

input_file=${1}
echo "input_file=${input_file}"

pwd

CMSSW_VERSION=CMSSW_12_5_0_pre4

source /cvmfs/cms.cern.ch/cmsset_default.sh
cmsrel ${CMSSW_VERSION}
cd ${CMSSW_VERSION}/src
eval `scramv1 runtime -sh`
git-cms-merge-topic slowmoyang:ge21-me21-seg-reco__from-CMSSW_12_5_0_pre4
scram b
cd -

#source /cvmfs/cms.cern.ch/cmsset_default.sh
#cd /pad/seyang/Projects/GEM-Workspace/SW-Dev/220722_GE21-ME21-Segment-Reco/CMSSW_12_5_0_pre4/
#eval `scramv1 runtime -sh`
#cd -

echo "SCRAM_ARCH=${SCRAM_ARCH}"
echo "CMSSW_VERSION=${CMSSW_VERSION}"
echo "CMSSW_BASE=${CMSSW_BASE}"

cfg_file=step2_RAW2DIGI_L1Reco_RECO_GEMCSCSegment.py
file_prepend="root://eoscms.cern.ch//eos/cms"
output_file="output.root"

cmsRun ${cfg_file} \
    inputFiles=${input_file} \
    filePrepend=${file_prepend} \
    outputFile=${output_file}

ls -lha .

stat ${output_file}

# hdfs dfs -put ${output_file} /user/seyang/GEM/SW-Dev/220722_GE21-ME21-Segment-Reco/test/CMSSW_12_5_0_pre4/reco-with-relval
