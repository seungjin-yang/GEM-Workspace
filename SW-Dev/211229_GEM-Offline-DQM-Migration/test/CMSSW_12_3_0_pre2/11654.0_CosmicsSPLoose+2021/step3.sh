#!/usr/bin/env sh



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
