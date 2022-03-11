#!/bin/sh
source setup.sh

CFG=step1_GEN_SIM.py
NUM_JOBS=10000

submit_empty ${CFG} ${NUM_JOBS}
