#!/usr/bin/env sh
SCRAM_ARCH=slc7_amd64_gcc900 cmsrel CMSSW_12_3_0_pre2
cd CMSSW_12_3_0_pre2/src
cmsenv
git-cms-merge-topic seungjin-yang:https://github.com/seungjin-yang/cmssw/tree/Moving-GEM-Offline-DQM__from-CMSSW_12_3_0_pre2
cd ../..
runTheMatrix.py -w upgrade -l 11650.0 # ZMM_14+2021
runTheMatrix.py -w upgrade -l 35050.0 # ZMM_14+2026D77
wget https://raw.githubusercontent.com/seungjin-yang/GEM-Workspace/main/SW-Dev/211229_GEM-Offline-DQM-Migration/test/CMSSW_12_3_0_pre2/11654.0_CosmicsSPLoose%2B2021/driver.sh -O 11654.0_CosmicsSPLoose+2021.sh
bash 11654.0.sh # CosmicsSPLoose+2021 with fix
