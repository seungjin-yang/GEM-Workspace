#!/usr/bin/env zsh
cfg_file=${CMSSW_BASE}/src/DQM/Integration/python/clients/gem_dqm_sourceclient-live_cfg.py
log_file=./unittest.log
cmsRun ${cfg_file} unitTest=True > ${log_file} 2>&1 &

print -- "sleep 3 sec"
sleep 3

print -- "reading ${log_file}"
tail -f ${log_file} | bat -l log --paging=never
