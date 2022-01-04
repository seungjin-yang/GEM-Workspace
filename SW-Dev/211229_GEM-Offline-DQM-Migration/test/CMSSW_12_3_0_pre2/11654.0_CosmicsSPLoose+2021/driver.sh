#!/usr/bin/env sh
cmsDriver.py UndergroundCosmicSPLooseMu_cfi  \
	--step GEN,SIM \
	--number 100000 \
	--conditions auto:phase1_2021_realistic \
	--beamspot Run3RoundOptics25ns13TeVLowSigmaZ \
	--datatier GEN-SIM \
	--eventcontent FEVTDEBUG \
	--geometry DB:Extended \
	--era Run3 \
	--scenario cosmics \
	--fileout file:step1.root \
    --python_filename step1_GEN_SIM.py \
    --nStreams 2 \
    --nThreads 8 \
> step1.log 2>&1 &

cmsDriver.py step2  \
	--step DIGI:pdigi_valid,L1,DIGI2RAW,HLT:@relval2021 \
	--conditions auto:phase1_2021_realistic \
	--datatier GEN-SIM-DIGI-RAW \
	--number -1 \
	--eventcontent FEVTDEBUG \
	--geometry DB:Extended \
	--era Run3 \
	--scenario cosmics \
	--filein  file:step1.root \
	--fileout file:step2.root \
    --nStreams 2 \
    --nThreads 8 \
> step2.log 2>&1 &

cmsDriver.py step3  \
	--step RAW2DIGI,L1Reco,RECO,DQM \
	--conditions auto:phase1_2021_realistic \
	--datatier GEN-SIM-RECO,DQMIO \
	--number -1 \
	--eventcontent RECOSIM,DQM \
	--geometry DB:Extended \
	--era Run3 \
	--scenario cosmics \
	--filein  file:step2.root \
	--fileout file:step3.root \
    --nStreams 2 \
    --nThreads 8 \
> step3.log 2>&1 &

cmsDriver.py step4  \
	--step HARVESTING:@standardDQM \
	--conditions auto:phase1_2021_realistic \
	--mc  \
	--geometry DB:Extended \
	--scenario pp \
	--filetype DQM \
	--era Run3 \
	--scenario cosmics \
	--number -1 \
	--filein file:step3_inDQM.root \
	--fileout file:step4.root \
> step4.log 2>&1 &
