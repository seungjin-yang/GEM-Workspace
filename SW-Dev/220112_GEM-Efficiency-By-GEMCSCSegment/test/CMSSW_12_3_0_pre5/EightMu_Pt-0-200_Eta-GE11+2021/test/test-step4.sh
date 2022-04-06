#!/usr/bin/env sh
CFG=step4_DQM.py
INPUT_FILE=file:/store/user/seyang/GEM/220112_GEM-Efficiency-By-GEMCSCSegment/CMSSW_12_3_0_pre5/EightMu_Pt-0-200_Eta-GE11+2021/step3_RAW2DIGI_L1Reco_RECO_RECOSIM_PAT/step3_0.root
LOG_FILE="./logs/step4.txt"

echo "CMSSW_BASE=${CMSSW_BASE}"

cmsRun ${CFG} inputFiles=${INPUT_FILE} > ${LOG_FILE} 2>&1 &

tail -f ${LOG_FILE}
