#!/bin/sh
source setup.sh

CFG=step1_GEN_SIM.py
NUM_JOBS=2000

submit_empty ${CFG} ${NUM_JOBS}
