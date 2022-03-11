#!/bin/sh
source setup.sh
PREV_CFG=step2_DIGI_L1_DIGI2RAW_HLT.py
CFG=step3_RAW2DIGI_L1Reco_RECO_RECOSIM.py
INPUT_DIR=/store/user/seyang/GEM/220112_GEM-Efficiency-By-GEMCSCSegment/CMSSW_12_3_0_pre5/UndergroundCosmicMuNoFilter0T+2021/step2_DIGI_L1_DIGI2RAW_HLT/
submit_pool ${PREV_CFG} ${CFG} ${INPUT_DIR}
