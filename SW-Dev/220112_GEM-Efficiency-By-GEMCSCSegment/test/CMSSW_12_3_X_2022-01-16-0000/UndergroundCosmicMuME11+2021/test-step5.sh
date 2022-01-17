CFG=step5_HARVESTING.py
INPUT_FILE=step4.root
FILE_PREPEND=file:

LOG_FILE=logs/test-step5.txt

cmsRun ${CFG} inputFiles=${INPUT_FILE} filePrepend=${FILE_PREPEND} > ${LOG_FILE} 2>&1 &
tail -f ${LOG_FILE}
