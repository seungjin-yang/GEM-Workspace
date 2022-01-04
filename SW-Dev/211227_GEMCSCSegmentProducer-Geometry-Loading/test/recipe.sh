#!/usr/bin/env sh
SCRAM_ARCH=slc7_amd64_gcc900 cmsrel CMSSW_12_3_0_pre2
cd CMSSW_12_3_0_pre2/src
cmsenv
git-cms-merge-topic seungjin-yang:Fix-GEMCSCSegmentProducer-Geometry-Loading__from-CMSSW_12_3_0_pre2
cd ../..
wget https://raw.githubusercontent.com/seungjin-yang/GEM-Workspace/main/SW-Dev/211227_GEMCSCSegmentProducer-Geometry-Loading/test/step3_RAW2DIGI_L1Reco_RECO.py
wget https://raw.githubusercontent.com/seungjin-yang/GEM-Workspace/main/SW-Dev/211227_GEMCSCSegmentProducer-Geometry-Loading/test/filelist-2021-ZMM-step2.txt
wget https://raw.githubusercontent.com/seungjin-yang/GEM-Workspace/main/SW-Dev/211227_GEMCSCSegmentProducer-Geometry-Loading/test/runGEMCSCSegmentAnalyzer_cfg.py
cmsRun step3_RAW2DIGI_L1Reco_RECO.py inputFiles_load=filelist-2021-ZMM-step2.txt outputFile=step3.root maxEvents=1000
cmsRun runGEMCSCSegmentAnalyzer_cfg.py inputFiles=step3.root
