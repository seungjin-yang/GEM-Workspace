#!/bin/sh
source setup.sh
PREV_CFG=step2_DIGI_L1_DIGI2RAW_HLT.py
CFG=step3_RAW2DIGI_L1Reco_RECO_RECOSIM.py
submit_pool ${PREV_CFG} ${CFG}
