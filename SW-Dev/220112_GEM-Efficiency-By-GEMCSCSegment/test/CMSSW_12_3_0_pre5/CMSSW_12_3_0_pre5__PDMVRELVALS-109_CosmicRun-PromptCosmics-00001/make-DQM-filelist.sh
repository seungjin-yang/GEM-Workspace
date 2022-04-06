source setup.sh

INPUT_DIR=${OUTPUT_ROOT}/step4_DQM
OUTPUT_FILE=filelist-DQM.txt
if [ -f ${OUTPUT_FILE} ]; then
    rm -vf ${OUTPUT_FILE}
fi

gem-dqm-make-file-list.py -o ${OUTPUT_FILE} ${INPUT_DIR}
wc -l ${OUTPUT_FILE}
