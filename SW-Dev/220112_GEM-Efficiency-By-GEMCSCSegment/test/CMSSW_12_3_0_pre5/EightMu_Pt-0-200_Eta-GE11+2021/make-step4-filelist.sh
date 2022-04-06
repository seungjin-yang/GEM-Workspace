source setup.sh

INPUT_DIR=${OUTPUT_ROOT}/step4_DQM
rm -vf filelist-step4_DQM.txt
gem-dqm-make-file-list.py ${INPUT_DIR}
wc -l filelist-step4_DQM.txt
