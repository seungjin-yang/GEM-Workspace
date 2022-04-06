#!/usr/bin/env sh
CFG=step4_DQM.py
CFG=step2_DIGI_L1_DIGI2RAW_HLT.py
INPUT_FILE=file:/store/user/seyang/GEM/220112_GEM-Efficiency-By-GEMCSCSegment/CMSSW_12_3_0_pre5/UndergroundCosmicMuNoFilter0T+2021/step1_GEN_SIM/step1_0.root
LOG_FILE="./logs/test-step2.txt"

echo "CMSSW_BASE=${CMSSW_BASE}"

cmsRun -n 10 ${CFG} inputFiles=${INPUT_FILE} > ${LOG_FILE} 2>&1 &

tail -f ${LOG_FILE}
