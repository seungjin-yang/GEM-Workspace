cfg_file=step2_L1REPACK_HLT.py
input_file=$(head -n 1 ./step1_dasquery.log)

typeset -m cfg_file
typeset -m input_file

cmsRun -n 10 ${cfg_file} inputFiles=${input_file} maxEvents=-1
