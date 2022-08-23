#!/usr/bin/env zsh
source /cvmfs/cms.cern.ch/cmsset_default.sh
cmssw_base=../../../CMSSW_12_5_0_pre4
cd ${cmssw_base}
eval `scramv1 runtime -sh`
cd -

# cmsRun
cfg_file=TestGEMCSCSegmentAnalyzer_cfg.py
input_file=/store/user/seyang/GEM/SW-Dev/220722_GE21-ME21-Segment-Reco/test/CMSSW_12_5_0_pre4/reco-with-relval/step2_RAW2DIGI_L1Reco_RECO_GEMCSCSegment/03a81988-755f-4792-8b2d-e0b365cbd1e7.root
file_prepend="file:"
output_file=TestGEMCSCSegmentAnalyzer.root
# log
log_file=./TestGEMCSCSegmentAnalyzer.log

cmsRun \
    ${cfg_file} \
    inputFiles=${input_file} \
    filePrepend=${file_prepend} \
    outputFile=${output_file} \
> ${log_file} 2>&1 &

print -- "sleep 3s..."
sleep 3

tail -f ${log_file} | bat -l log --paging=never
