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
