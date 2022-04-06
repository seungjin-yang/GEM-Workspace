#!/usr/bin/env sh
source setup.sh

cmsDriver.py step4 \
	--conditions auto:run3_data_prompt \
	--data \
	--datatier DQMIO \
	--era Run3 \
	--eventcontent DQM \
	--no_exec \
	--number -1 \
	--scenario cosmics \
	--step DQM:gemEfficiencyAllSourcesCosmics+gemEffByGEMCSCSegment \
    --filein file:step3.root \
    --fileout file:step4.root

cmsDriver.py step5 \
	--conditions auto:run3_data_prompt \
	--data \
	--era Run3 \
	--filetype DQM \
	--no_exec \
	--number -1 \
	--scenario cosmics \
	--step HARVESTING:gemEfficiencyAllClientsCosmics+GEMDQMHarvester \
    --filein file:step4.root \
    --fileout file:step5.root
