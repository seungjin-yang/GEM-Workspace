cmsDriver.py GEMDQMUtils/Generator/python/EightMu_Pt-0-200_Eta-GE11_pythia8_cfi \
	--step GEN,SIM \
	--number 100 \
	--conditions auto:phase1_2021_realistic \
	--beamspot Run3RoundOptics25ns13TeVLowSigmaZ \
	--datatier GEN-SIM \
	--eventcontent FEVTDEBUG \
	--geometry DB:Extended \
	--era Run3 \
	--fileout file:step1.root \
    --python_filename step1_GEN_SIM.py \
    --no_exec

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

cmsDriver.py step3  \
	--step DQM:gemEfficiencyAllSources+gemEffByGEMCSCSegment \
	--conditions auto:phase1_2021_realistic \
	--datatier DQMIO \
	--number -1 \
	--eventcontent DQM \
	--geometry DB:Extended \
	--era Run3 \
	--filein  file:step2.root  \
	--fileout file:step3.root \
    --mc \
    --no_exec

cmsDriver.py step4  \
	--step HARVESTING:gemEfficiencyAllClients+GEMDQMHarvester \
	--conditions auto:phase1_2021_realistic \
	--mc  \
	--geometry DB:Extended \
	--scenario pp \
	--filetype DQM \
	--era Run3 \
	--number -1  \
	--filein file:step3_inDQM.root \
	--fileout file:step4.root \
    --no_exec
