for EACH in $(cat logs/wrong-step2_DIGI_L1_DIGI2RAW_HLT.txt)
do
    rm -vf ${EACH}
done
