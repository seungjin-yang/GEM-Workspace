cmsDriver.py TenMuExtendedE_0_200_pythia8_cfi  \
	--step GEN,SIM \
	--number 10 \
	--conditions auto:phase1_2021_realistic \
	--beamspot Run3RoundOptics25ns13TeVLowSigmaZ \
	--datatier GEN-SIM \
	--eventcontent FEVTDEBUG \
	--geometry DB:Extended \
	--era Run3 \
	--fileout file:step1.root \
    --no_exec \
    --python_filename step1_GEN_SIM.py

cmsDriver.py step2  \
	--step DIGI:pdigi_valid,L1,DIGI2RAW,HLT:@relval2021 \
	--conditions auto:phase1_2021_realistic \
	--datatier GEN-SIM-DIGI-RAW \
	--number -1 \
	--eventcontent FEVTDEBUGHLT \
	--geometry DB:Extended \
	--era Run3 \
	--filein  file:step1.root  \
	--fileout file:step2.root \
    --no_exec

cmsDriver.py step3  \
	--step RAW2DIGI,L1Reco,RECO \
	--conditions auto:phase1_2021_realistic \
	--datatier GEN-SIM-RECO \
	--number -1 \
	--eventcontent RECOSIM \
	--geometry DB:Extended \
	--era Run3 \
	--filein  file:step2.root  \
	--fileout file:step3.root \
    --no_exec
