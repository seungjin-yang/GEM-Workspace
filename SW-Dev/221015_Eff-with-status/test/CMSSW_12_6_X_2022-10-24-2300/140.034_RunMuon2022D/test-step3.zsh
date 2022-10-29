cfg_file=./step3_RAW2DIGI_L1Reco_RECO.py
# input_file=file:./step2.root
input_file=file:/eos/user/s/seyang/store/GEM/step2/fd94730f-edda-474c-b89f-cd815dacde9a.root
output_file=./step3.root
max_events=-1

typeset -m cfg_file
typeset -m input_file

cmsRun -n 10 ${cfg_file} inputFiles=${input_file} outputFile=${output_file} maxEvents=${max_events}
