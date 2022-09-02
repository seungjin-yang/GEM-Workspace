#!/usr/bin/env zsh

cmssw_base=../../../CMSSW_12_4_7
cfg_file=gemcscSegments_cfg.py
input_file=$(head -n 1 ./input-files.txt)
file_prepend=root://eoscms.cern.ch//eos/cms/tier0/

if [ ! -d ${cmssw_base} ]; then
    print -- "cmssw_base not found: ${cmssw_base}"
    return 1
fi

cd ${cmssw_base}
eval `scramv1 runtime -sh`
cd -

log_file=test-${cfg_file:t:r}.log

cmsRun ${cfg_file} \
    inputFiles=${input_file} \
    filePrepend=${file_prepend} \
    maxEvents=10 \
> ${log_file} 2>&1 &

print -- "sleep 3 sec"
sleep 3

tail -f ${log_file} | bat -l log --paging=never
