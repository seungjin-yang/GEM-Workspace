#!/bin/sh

# modified from https://cms-pdmv.cern.ch/relval/api/relvals/get_cmsdriver/CMSSW_12_3_0_pre2__UPSG_Std_2026D77noPU-ZMM_14-00001

cmsDriver.py runGEMCSCSegmentProducer \
	--conditions 122X_mcRun4_realistic_v4 \
	--customise SLHCUpgradeSimulations/Configuration/aging.customise_aging_1000 \
	--datatier GEN-SIM-RECO \
	--era Phase2C11I13M9 \
	--eventcontent FEVTDEBUGHLT \
	--filein "file:step3.root" \
	--fileout "file:step4.root" \
	--geometry Extended2026D77 \
	--no_exec \
	--number -1 \
	--step RECO
