#!/bin/sh
source setup.sh
PREV_CFG=step3_RAW2DIGI_L1Reco_RECO.py
CFG=step4_DQM.py
submit_pool ${PREV_CFG} ${CFG}
