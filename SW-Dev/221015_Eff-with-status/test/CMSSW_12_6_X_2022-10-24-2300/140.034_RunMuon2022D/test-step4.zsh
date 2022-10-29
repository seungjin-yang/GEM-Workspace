cfg_file=./step4_DQM.py
input_file=file:./step3.root
# input_file=file:/eos/user/s/seyang/store/GEM/step3/709a03e4-531a-48ba-b31d-a56daf75ad61.root

typeset -m cfg_file
typeset -m input_file

cmsRun -n 10 ${cfg_file} inputFiles=${input_file}
