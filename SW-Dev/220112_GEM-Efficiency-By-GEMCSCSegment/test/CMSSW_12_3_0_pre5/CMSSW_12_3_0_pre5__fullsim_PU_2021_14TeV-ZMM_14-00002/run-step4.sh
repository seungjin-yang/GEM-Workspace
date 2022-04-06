#!/usr/bin/env sh
source setup.sh

CFG=step4_DQM.py
INPUT_FILE=file:/store/scratch/seyang/relval/CMSSW_12_3_0_pre5/RelValZMM_14/GEN-SIM-RECO/PU_123X_mcRun3_2021_realistic_v6-v1/10000/26c27aad-f2e9-4bef-9ac1-cb49f7890aaf.root
LOG_FILE="./logs/step4.txt"

cmsRun ${CFG} inputFiles=${INPUT_FILE} > ${LOG_FILE} 2>&1 &

tail -f ${LOG_FILE}
