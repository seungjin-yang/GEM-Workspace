#!/usr/bin/env sh
source setup.sh

CONDITIONS=auto:phase1_2021_cosmics
SCENARIO=cosmics
ERA=Run3
GEOMETRY=DB:Extended
MAG_FIELD=0T

COMMON_OPTIONS="--mc --conditions ${CONDITIONS} --era ${ERA} --scenario ${SCENARIO} --geometry ${GEOMETRY} --magField ${MAG_FIELD} --no_exec"

cmsDriver.py GEMDQMUtils/Generator/python/UndergroundCosmicMuNoFilter_cfi \
    ${COMMON_OPTIONS} \
	--step GEN,SIM \
	--number 50000 \
	--beamspot Run3RoundOptics25ns13TeVLowSigmaZ \
	--datatier GEN-SIM \
	--eventcontent FEVTDEBUG \
	--fileout file:step1.root \
    --python_filename step1_GEN_SIM.py


cmsDriver.py step2  \
    ${COMMON_OPTIONS} \
	--step DIGI:pdigi_valid,L1,DIGI2RAW,HLT:@relval2021 \
	--datatier GEN-SIM-DIGI-RAW \
	--number -1 \
	--eventcontent FEVTDEBUG \
	--filein  file:step1.root  \
	--fileout file:step2.root

cmsDriver.py step3  \
    ${COMMON_OPTIONS} \
	--step RAW2DIGI,L1Reco,RECO,RECOSIM \
	--datatier GEN-SIM-RECO \
	--number -1 \
	--eventcontent FEVT \
	--filein  file:step2.root  \
	--fileout file:step3.root

cmsDriver.py step4 \
    ${COMMON_OPTIONS} \
	--step DQM:gemEfficiencyAllSourcesCosmics \
	--datatier DQMIO \
	--number -1 \
	--eventcontent DQM \
	--filein  file:step3.root  \
	--fileout file:step4.root


cmsDriver.py step5  \
    ${COMMON_OPTIONS} \
	--step HARVESTING:gemEfficiencyAllClientsCosmics \
	--mc  \
	--filetype DQM \
	--number -1  \
	--filein file:step4.root \
	--fileout file:step5.root
