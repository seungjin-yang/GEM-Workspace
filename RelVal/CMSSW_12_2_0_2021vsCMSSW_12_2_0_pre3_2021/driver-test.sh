# https://cms-pdmv.cern.ch/relval/api/relvals/get_cmsdriver/CMSSW_12_2_0_pre3__fullsim_noPU_2021_14TeV-SingleMuPt10-00003

cmsDriver.py step3 \
	--conditions 122X_mcRun3_2021_realistic_v5 \
	--datatier GEN-SIM-RECO,MINIAODSIM,NANOAODSIM,DQMIO \
	--era Run3,run3_nanoAOD_devel \
	--eventcontent RECOSIM,MINIAODSIM,NANOEDMAODSIM,DQM \
	--filein "file:step2.root" \
	--fileout "file:step3.root" \
	--geometry DB:Extended \
	--no_exec \
	--number 10 \
	--python_filename test_step3_cfg.py \
	--step RAW2DIGI,L1Reco,RECO,RECOSIM,EI,PAT,NANO,VALIDATION:@standardValidation+@miniAODValidation,DQM:@standardDQM+@ExtraHLT+@miniAODDQM+@nanoAODDQM \
	--no_exec

cmsDriver.py step4 \
	--conditions 122X_mcRun3_2021_realistic_v5 \
	--era Run3,run3_nanoAOD_devel \
	--filein "file:step3_inDQM.root" \
	--fileout "file:step4.root" \
	--filetype DQM \
	--geometry DB:Extended \
	--mc \
	--no_exec \
	--number 10 \
	--python_filename test_step4_cfg.py \
	--scenario pp \
	--step HARVESTING:@standardValidation+@standardDQM+@ExtraHLT+@miniAODValidation+@miniAODDQM+@nanoAODDQM \
	--no_exec
