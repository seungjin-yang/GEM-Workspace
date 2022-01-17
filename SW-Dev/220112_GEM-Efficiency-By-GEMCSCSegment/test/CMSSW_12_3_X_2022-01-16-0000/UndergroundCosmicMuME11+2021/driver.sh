#!/usr/bin/env sh
CONDITIONS=auto:phase1_2021_cosmics
SCENARIO=cosmics
ERA=Run3
GEOMETRY=DB:Extended
MAG_FIELD=0T

COMMON_ARGS="--mc --conditions ${CONDITIONS} --era ${ERA} --scenario ${SCENARIO} --geometry ${GEOMETRY} --magField ${MAG_FIELD}"

cmsDriver.py GEMDQMUtils/Generator/python/UndergroundCosmicMuME11_cfi \
    ${COMMON_ARGS} \
    --step GEN,SIM \
    --number 50000 \
    --beamspot Run3RoundOptics25ns13TeVLowSigmaZ \
    --datatier GEN-SIM \
    --eventcontent FEVTDEBUG \
    --fileout file:step1.root \
    --python_filename step1_GEN_SIM.py \
    --no_exec

cmsDriver.py step2 \
    ${COMMON_ARGS} \
    --step DIGI:pdigi_valid,L1,DIGI2RAW,HLT:@relval2021 \
    --datatier GEN-SIM-DIGI-RAW \
    --number -1 \
    --eventcontent FEVTDEBUG \
    --filein file:step1.root \
    --fileout file:step2.root \
    --no_exec

cmsDriver.py step3 \
    ${COMMON_ARGS} \
    --step RAW2DIGI,L1Reco,RECO \
    --datatier GEN-SIM-RECO \
    --number -1 \
    --eventcontent FEVT \
    --filein file:step2.root \
    --fileout file:step3.root \
    --no_exec
