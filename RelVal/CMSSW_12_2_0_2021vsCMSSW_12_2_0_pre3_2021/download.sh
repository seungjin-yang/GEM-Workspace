XRD_URL=root://eoscms.cern.ch//eos/cms/

for EACH in $(cat ./reference_GEN-SIM-DIGI-RAW.txt)
do
    OUTPUT_DIR=$(dirname ${EACH})
    OUTPUT_DIR=${OUTPUT_DIR/"/store/"/"/store/scratch/seyang/"}
    if [ ! -d ${OUTPUT_DIR} ]; then
        mkdir -vp ${OUTPUT_DIR}
    fi

    xrdcp -v ${XRD_URL}/${EACH} ${OUTPUT_DIR}
done
