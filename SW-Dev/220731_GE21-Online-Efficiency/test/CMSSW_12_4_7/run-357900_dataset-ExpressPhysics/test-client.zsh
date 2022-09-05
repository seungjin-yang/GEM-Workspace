#!/usr/bin/env zsh

cmssw_base=../../../CMSSW_12_4_7
cfg_file=./gemEffByGEMCSCSegmentClient_cfg.py
input_file=./output.root
file_prepend="file:"
max_events=-1

if [ ! -d ${cmssw_base} ]; then
    print -- "cmssw_base not found: ${cmssw_base}"
    return 1
fi

if [ ! -f ${cfg_file} ]; then
    print -- "cfg_file not found: ${cfg_file}"
    return 1
fi

cd ${cmssw_base}
eval `scramv1 runtime -sh`
cd -

log_file=test-${cfg_file:t:r}.log

cmsRun ${cfg_file} \
    inputFiles=${input_file} \
    filePrepend=${file_prepend} \
    maxEvents=${max_events} \
> ${log_file} 2>&1 &

print -- "sleep 3 sec"
sleep 3

tail -f ${log_file} | bat -l log --paging=never
