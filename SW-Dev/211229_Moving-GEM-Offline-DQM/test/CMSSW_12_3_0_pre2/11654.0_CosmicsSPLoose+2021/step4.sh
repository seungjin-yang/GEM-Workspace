#!/usr/bin/env sh
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
