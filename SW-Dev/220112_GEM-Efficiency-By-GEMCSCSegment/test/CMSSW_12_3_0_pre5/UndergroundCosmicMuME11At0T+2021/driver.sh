#!/usr/bin/env sh
source setup.sh

CONDITIONS=auto:phase1_2021_cosmics
SCENARIO=cosmics
ERA=Run3
GEOMETRY=DB:Extended
MAG_FIELD=0T

COMMON_OPTIONS="--mc --conditions ${CONDITIONS} --era ${ERA} --scenario ${SCENARIO} --geometry ${GEOMETRY} --magField ${MAG_FIELD} --no_exec"

cmsDriver.py step4 \
    ${COMMON_OPTIONS} \
	--step DQM:gemEfficiencySourcesCosmics+gemEffByGEMCSCSegment \
	--datatier DQMIO \
	--number -1 \
	--eventcontent DQM \
	--filein  file:step3.root  \
	--fileout file:step4.root


cmsDriver.py step5  \
    ${COMMON_OPTIONS} \
	--step HARVESTING:gemEfficiencyClientsCosmics+GEMDQMHarvester \
	--mc  \
	--filetype DQM \
	--number -1  \
	--filein file:step4.root \
	--fileout file:step5.root
