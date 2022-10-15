cmsDriver.py TenMuExtendedE_0_200_pythia8_cfi  \
	--step GEN,SIM \
	--number 100 \
	--conditions auto:phase1_2023_realistic \
	--beamspot Realistic25ns13p6TeVEarly2022Collision \
	--datatier GEN-SIM \
	--eventcontent FEVTDEBUG \
	--geometry DB:Extended \
	--era Run3 \
	--fileout file:step1.root \
    --python_filename step1_GEN_SIM.py \
    --no_exec
 
cmsDriver.py step2  \
	--step DIGI:pdigi_valid,L1,DIGI2RAW,HLT:@relval2022 \
	--conditions auto:phase1_2023_realistic \
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
	--conditions auto:phase1_2023_realistic \
	--datatier GEN-SIM-RECO \
	--number -1 \
	--eventcontent RECOSIM \
	--geometry DB:Extended \
	--era Run3 \
	--filein  file:step2.root  \
	--fileout file:step3.root  \
    --no_exec

cmsDriver.py step4  \
	--step DQM:gemSources \
	--conditions auto:phase1_2023_realistic \
	--datatier DQMIO \
	--number -1 \
	--eventcontent DQM \
	--geometry DB:Extended \
	--era Run3 \
	--filein  file:step3.root  \
	--fileout file:step4.root  \
    --no_exec


 
 cmsDriver.py step5  \
	--step HARVESTING:gemClients \
	--conditions auto:phase1_2023_realistic \
	--mc  \
	--geometry DB:Extended \
	--scenario pp \
	--filetype DQM \
	--era Run3 \
	--number -1  \
	--filein file:step4.root \
	--fileout file:step5.root  \
    --no_exec

