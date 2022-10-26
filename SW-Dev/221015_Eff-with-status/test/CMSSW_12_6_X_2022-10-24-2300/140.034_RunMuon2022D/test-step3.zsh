cfg_file=./step3_RAW2DIGI_L1Reco_RECO.py
input_file=file:./step2.root

typeset -m cfg_file
typeset -m input_file

cmsRun -n 10 ${cfg_file} inputFiles=${input_file}
