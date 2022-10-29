cfg_file=./step4_DQM.py
input_file=file:./step3.root

typeset -m cfg_file
typeset -m input_file

cmsRun -n 5 ${cfg_file} inputFiles=${input_file} maxEvents=1000
