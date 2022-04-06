#!/usr/bin/env sh
source setup.sh

CFG=step4_DQM.py
INPUT_FILE=file:/store/scratch/seyang/relval/CMSSW_12_3_0_pre5/ExpressCosmics/RECO/123X_dataRun3_Prompt_v2_RelVal_2021GR5-v1/10000/026ad796-07f5-4ddb-9851-ab73d7ac3b9c.root
LOG_FILE="./logs/test-step4.txt"

cmsRun ${CFG} inputFiles=${INPUT_FILE} > ${LOG_FILE} 2>&1 &

tail -f ${LOG_FILE}
