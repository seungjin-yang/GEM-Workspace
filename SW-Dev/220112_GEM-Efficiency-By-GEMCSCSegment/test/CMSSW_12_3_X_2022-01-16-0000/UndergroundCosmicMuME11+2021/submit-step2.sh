#!/bin/sh
source setup.sh
PREV_CFG=step1_GEN_SIM.py
CFG=step2_DIGI_L1_DIGI2RAW_HLT.py
submit_pool ${PREV_CFG} ${CFG}
