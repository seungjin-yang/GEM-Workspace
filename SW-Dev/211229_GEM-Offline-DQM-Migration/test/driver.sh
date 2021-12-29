#!/usr/bin/env sh

# Copied from https://cms-pdmv.cern.ch/relval/api/relvals/get_cmsdriver/CMSSW_12_3_0_pre2__fullsim_noPU_2021_14TeV-ZMM_14-00001

cmsDriver.py step4 \
	--conditions auto:phase1_2021_realistic \
	--datatier DQMIO \
	--era Run3 \
	--eventcontent DQM \
	--filein "file:step3.root" \
	--fileout "file:step4.root" \
	--geometry DB:Extended \
	--no_exec \
	--number -1 \
	--step VALIDATION:@standardValidation,DQM:@standardDQM

cmsDriver.py step5 \
	--conditions auto:phase1_2021_realistic \
	--era Run3 \
	--filein "file:step3_inDQM.root" \
	--fileout "file:step4.root" \
	--filetype DQM \
	--geometry DB:Extended \
	--mc \
	--no_exec \
	--number -1 \
	--scenario pp \
	--step HARVESTING:@standardValidation+@standardDQM
