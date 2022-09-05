#!/usr/bin/env zsh
module load lxbatch/spool

input_file_list_array=(
    "./input-files/x00.txt"
    "./input-files/x01.txt"
    "./input-files/x02.txt"
)

for input_file_list in 
do
    condor_submit -spool lxplus.condor input_file_list=${input_file_list}
done

module unload lxbatch/spool
