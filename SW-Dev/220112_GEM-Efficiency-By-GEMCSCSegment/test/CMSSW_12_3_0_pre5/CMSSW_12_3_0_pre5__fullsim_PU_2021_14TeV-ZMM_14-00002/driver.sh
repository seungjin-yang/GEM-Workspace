source setup.sh

cmsDriver.py step4 \
	--conditions auto:phase1_2021_realistic \
	--datatier DQMIO \
	--era Run3 \
	--eventcontent DQM \
	--filein "file:step3.root" \
	--fileout "file:step4.root" \
	--geometry DB:Extended \
	--no_exec \
	--number -1 \
    --mc \
	--scenario pp \
	--step DQM:gemEfficiencySources+gemEffByGEMCSCSegment

cmsDriver.py step5 \
	--conditions auto:phase1_2021_realistic \
	--era Run3 \
	--filein "file:step4.root" \
	--fileout "file:step5.root" \
	--filetype DQM \
	--geometry DB:Extended \
	--mc \
	--no_exec \
	--number -1 \
	--scenario pp \
	--step HARVESTING:gemEfficiencyClients+GEMDQMHarvester
