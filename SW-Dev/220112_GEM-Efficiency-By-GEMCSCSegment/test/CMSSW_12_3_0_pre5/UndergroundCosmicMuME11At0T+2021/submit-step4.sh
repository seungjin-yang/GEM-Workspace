#!/bin/sh
source setup.sh
PREV_CFG=none
CFG=step4_DQM.py
INPUT_DIR=/store/user/seyang/GEM/220118_Update-GEMEfficiencyAnalyzer/CMSSW_12_3_0_pre5/UndergroundCosmicMuME11At0T+2021/step3_RAW2DIGI_L1Reco_RECO_RECOSIM
submit_pool ${PREV_CFG} ${CFG} ${INPUT_DIR}
