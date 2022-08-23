#!/usr/bin/env zsh

cd ../../../CMSSW_12_5_0_pre4
eval `scramv1 runtime -sh`
cd -

cfg_file=step2_RAW2DIGI_L1Reco_RECO_GEMCSCSegment.py
input_file=$(head -n 1 ./filelist.txt)
file_prepend="root://eoscms.cern.ch//eos/cms"
log_file=test-step2_RAW2DIGI_L1Reco_RECO_GEMCSCSegment.log

cmsRun ${cfg_file} \
    inputFiles=${input_file} \
    filePrepend=${file_prepend} \
    maxEvents=10 \
> ${log_file} 2>&1 &

print -- "sleep 3 sec"
sleep 3

tail -f ${log_file} | bat -l log --paging=never
