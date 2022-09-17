#!/usr/bin/env zsh
# https://cms-pdmv.cern.ch/relval/api/relvals/get_cmsdriver/CMSSW_12_6_0_pre2__AUTOMATED_fullsim_noPU_2022_14TeV-ZMM_14-00001

cmsDriver.py TenMuE_0_200_pythia8_cfi \
	--beamspot Realistic25ns13p6TeVEarly2022Collision \
	--conditions auto:phase1_2022_realistic \
	--datatier GEN-SIM \
	--era Run3 \
	--eventcontent FEVTDEBUG \
	--fileout "file:step1.root" \
	--geometry DB:Extended \
	--no_exec \
	--number 1000 \
	--python_filename step_GEN_SIM.py \
	--step GEN,SIM 


cmsDriver.py step2 \
	--conditions auto:phase1_2022_realistic \
	--datatier GEN-SIM-DIGI-RAW \
	--era Run3 \
	--eventcontent FEVTDEBUGHLT \
	--filein "file:step1.root" \
	--fileout "file:step2.root" \
	--geometry DB:Extended \
	--no_exec \
	--number -1 \
	--step DIGI:pdigi_valid,L1,DIGI2RAW,HLT:@relval2022

cmsDriver.py step3 \
	--conditions auto:phase1_2022_realistic \
	--datatier GEN-SIM-RECO \
	--era Run3 \
	--eventcontent RECO \
	--filein "file:step2.root" \
	--fileout "file:step3.root" \
	--geometry DB:Extended \
	--no_exec \
	--number -1 \
	--step RAW2DIGI,L1Reco,RECO
