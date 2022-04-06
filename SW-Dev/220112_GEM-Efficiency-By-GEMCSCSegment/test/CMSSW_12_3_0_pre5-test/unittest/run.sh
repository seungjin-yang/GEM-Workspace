#!/usr/bin/env sh
CFG_FILE=/pad/seyang/Projects/GEM-Workspace/SW-Dev/220112_GEM-Efficiency-By-GEMCSCSegment/CMSSW_12_3_0_pre5-test/src/DQM/Integration/python/clients/gem_dqm_sourceclient-live_cfg.py
LOG_FILE=./unittest.log
cmsRun ${CFG_FILE} unitTest=True > ${LOG_FILE} 2>&1 &
tail -f ${LOG_FILE}
