#!/bin/sh
source setup.sh
PREV_CFG=step3_RAW2DIGI_L1Reco_RECO_RECOSIM__SMALL.py
CFG=step4_DQM__SMALL.py
submit_pool ${PREV_CFG} ${CFG}
