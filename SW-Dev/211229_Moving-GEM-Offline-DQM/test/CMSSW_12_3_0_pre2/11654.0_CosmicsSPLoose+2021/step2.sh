#!/usr/bin/env sh
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
