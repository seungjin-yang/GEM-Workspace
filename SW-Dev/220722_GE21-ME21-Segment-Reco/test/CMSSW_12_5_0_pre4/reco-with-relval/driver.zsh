#!/usr/bin/env zsh

# https://cms-pdmv.cern.ch/relval/api/relvals/get_cmsdriver/CMSSW_12_5_0_pre4__AUTOMATED_fullsim_PU_2022_14TeV_RECOonly-ZMM_14-00002

cd ../../../CMSSW_12_5_0_pre4
eval `scramv1 runtime -sh`
cd -

cmsDriver.py step2 \
	--conditions auto:phase1_2022_realistic \
	--datatier GEN-SIM-RECO \
	--era Run3 \
	--eventcontent RECOSIM \
	--filein "dbs:/RelValZMM_14/CMSSW_12_5_0_pre3-PU_124X_mcRun3_2022_realistic_v8-v1/GEN-SIM-DIGI-RAW" \
	--fileout "file:step2.root" \
	--geometry DB:Extended \
	--no_exec \
	--number -1 \
	--step RAW2DIGI,L1Reco,RECO
