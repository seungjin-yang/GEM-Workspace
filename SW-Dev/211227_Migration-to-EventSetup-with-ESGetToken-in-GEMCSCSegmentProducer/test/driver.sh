#!/bin/sh

# modified from https://cms-pdmv.cern.ch/relval/api/relvals/get_cmsdriver/CMSSW_12_3_0_pre2__fullsim_PU_2021_14TeV-ZMM_14-00001

cmsDriver.py step3 \
	--conditions auto:phase1_2021_realistic \
	--datatier GEN-SIM-RECO \
	--era Run3 \
	--eventcontent RECOSIM \
	--filein "file:step2.root" \
	--fileout "file:step3.root" \
	--geometry DB:Extended \
	--no_exec \
	--number -1 \
	--step RAW2DIGI,L1Reco,RECO
