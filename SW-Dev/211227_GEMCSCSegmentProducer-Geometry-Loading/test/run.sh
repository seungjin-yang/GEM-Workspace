#!/usr/bin/env sh
CFG=runGEMCSCSegmentProducer_RECO.py
INPUT_FILE_LIST=./filelist.txt
INPUT_FILE=$(head -n 1 ${INPUT_FILE_LIST})
XROOTD_URL=root://eoscms.cern.ch//eos/cms/

COMMAND="cmsRun ${CFG} inputFiles=${INPUT_FILE} filePrepend=${XROOTD_URL}"
echo ${COMMAND}
eval ${COMMAND}
