#!/usr/bin/env sh
source setup.sh

CFG=step4_DQM.py
# INPUT_FILE=file:/store/scratch/seyang/GEM/220118_Update-GEMEfficiencyAnalyzer/CMSSW_12_3_0_pre5/UndergroundCosmicMuME11At0T+2021/step3_RAW2DIGI_L1Reco_RECO_RECOSIM/step3_0.root
INPUT_FILE=file:/pad/seyang/Projects/GEM-Workspace/SW-Dev/220118_Update-GEMEfficiencyAnalyzer/test/CMSSW_12_3_0_pre5/UndergroundCosmicMuME11At0T+2021/step3.root
LOG_FILE="./logs/step4.txt"

cmsRun ${CFG} inputFiles=${INPUT_FILE} > ${LOG_FILE} 2>&1 &

tail -f ${LOG_FILE}
