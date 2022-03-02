#!/bin/sh
source setup.sh
PREV_CFG=none
CFG=step4_DQM.py
INPUT_DIR=/store/scratch/seyang/relval/CMSSW_12_3_0_pre5/RelValZMM_14/GEN-SIM-RECO/PU_123X_mcRun3_2021_realistic_v6-v1/10000/
submit_pool ${PREV_CFG} ${CFG} ${INPUT_DIR}
