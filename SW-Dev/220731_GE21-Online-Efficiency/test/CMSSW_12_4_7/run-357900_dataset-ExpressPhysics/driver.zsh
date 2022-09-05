#!/usr/bin/env zsh

# https://cms-pdmv.cern.ch/relval/api/relvals/get_cmsdriver/CMSSW_12_5_0_pre4__AUTOMATED_fullsim_PU_2022_14TeV_RECOonly-ZMM_14-00002

cd ../../../CMSSW_12_4_7
eval `scramv1 runtime -sh`
cd -

global_tag="124X_dataRun3_Express_v5"

function build-source() {
cmsDriver.py gemEffByGEMCSCSegmentSource \
    --conditions ${global_tag} \
    --datatier DQMIO \
    --era Run3 \
    --eventcontent DQM \
    --filein "file:input.root" \
    --fileout "file:output.root" \
    --geometry DB:Extended \
    --no_exec \
    --number -1 \
    --step DQM:gemEffByGEMCSCSegmentSource \
    --python_filename gemEffByGEMCSCSegmentSource_cfg.py
}

function build-client() {
cmsDriver.py gemEffByGEMCSCSegmentClient \
	--conditions ${global_tag} \
    --filetype DQM \
	--era Run3 \
	--eventcontent DQM \
	--filein "file:input.root" \
	--fileout "file:output.root" \
	--geometry DB:Extended \
	--no_exec \
	--number -1 \
	--step HARVESTING:gemEffByGEMCSCSegmentClient \
    --python_filename gemEffByGEMCSCSegmentClient_cfg.py
}

build-source
build-client
