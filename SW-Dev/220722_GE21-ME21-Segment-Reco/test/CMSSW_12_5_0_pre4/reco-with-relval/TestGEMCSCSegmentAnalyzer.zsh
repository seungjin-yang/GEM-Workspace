#!/usr/bin/env zsh
cmssw_base=../../../CMSSW_12_5_0_pre4
cfg_file=TestGEMCSCSegmentAnalyzer_cfg.py
log_file=./TestGEMCSCSegmentAnalyzer.log
input_file=./gemcscSegments.root

cd ${cmssw_base}
eval `scramv1 runtime -sh`
cd -

cmsRun ${cfg_file} inputFiles=${input_file} filePrepend=file: > ${log_file} 2>&1 &

print -- "sleep 3s..."
sleep 3

tail -f ${log_file} | bat -l log --paging=never
