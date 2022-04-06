#!/bin/sh
source setup.sh
PREV_CFG=none
CFG=step4_DQM.py
INPUT_DIR=/store/scratch/seyang/relval/CMSSW_12_3_0_pre5/ExpressCosmics/RECO/123X_dataRun3_Prompt_v2_RelVal_2021GR5-v1/10000
submit_pool ${PREV_CFG} ${CFG} ${INPUT_DIR}
