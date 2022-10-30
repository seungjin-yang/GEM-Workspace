#!/usr/bin/env zsh
config_file=./step5_HARVESTING.py
input_file=./filelist-step4.txt
file_prepend=file:
max_events=-1

typeset -m config_file
typeset -m input_file

cmsRun \
    ${config_file} \
    inputFiles_load=${input_file} \
    filePrepend=${file_prepend} \
    maxEvents=${max_events}
