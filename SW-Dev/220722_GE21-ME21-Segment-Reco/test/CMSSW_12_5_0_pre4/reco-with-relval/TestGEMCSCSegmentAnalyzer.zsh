#!/usr/bin/env zsh
# setup
cmssw_base=../../../CMSSW_12_5_0_pre4
cd ${cmssw_base}
eval `scramv1 runtime -sh`
cd -

# cmsRun
cfg_file=TestGEMCSCSegmentAnalyzer_cfg.py
input_file=./step2.root
output_file=TestGEMCSCSegmentAnalyzer.root
# log
log_file=./TestGEMCSCSegmentAnalyzer.log

cmsRun \
    ${cfg_file} \
    inputFiles=${input_file} \
    filePrepend=file: \
    outputFile=${output_file} \
> ${log_file} 2>&1 &

print -- "sleep 3s..."
sleep 3

tail -f ${log_file} | bat -l log --paging=never
