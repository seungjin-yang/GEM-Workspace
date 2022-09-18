#!/usr/bin/env zsh

cmsDriver.py TenMuExtendedE_0_200_pythia8_cfi  \
	--step GEN,SIM \
	--number 1000 \
	--conditions auto:phase2_realistic_T21 \
	--beamspot HLLHC \
	--datatier GEN-SIM \
	--eventcontent FEVTDEBUG \
	--geometry Extended2026D94 \
	--era Phase2C18I13M9 \
	--fileout file:step1.root \
    --python_filename step1_GEN_SIM.py \
    --no_exec
 
 cmsDriver.py step2  \
	--step DIGI:pdigi_valid,L1TrackTrigger,L1,DIGI2RAW,HLT:@fake2 \
	--conditions auto:phase2_realistic_T21 \
	--datatier GEN-SIM-DIGI-RAW \
	--number -1 \
	--eventcontent FEVTDEBUGHLT \
	--geometry Extended2026D94 \
	--era Phase2C18I13M9 \
	--filein  file:step1.root  \
	--fileout file:step2.root  \
    --no_exec
 
 cmsDriver.py step3  \
	--step RAW2DIGI,RECO \
	--conditions auto:phase2_realistic_T21 \
	--datatier GEN-SIM-RECO \
	--number -1 \
	--eventcontent FEVTDEBUGHLT \
	--geometry Extended2026D94 \
	--era Phase2C18I13M9 \
	--filein  file:step2.root  \
	--fileout file:step3.root  \
    --no_exec
