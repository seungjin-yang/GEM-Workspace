# Online GE1/1 Efficiency Monitoring with GEMCSCSegment
## Description
`TODO`

## Setup
```bash
source /cvmfs/cms.cern.ch/cmsset_default.sh
SCRAM_ARCH=slc7_amd64_gcc900 cmsrel CMSSW_12_3_0_pre5
cd CMSSW_12_3_0_pre5/src
cmsenv
git-cms-addpkg DQM/Integration
git-cms-merge-topic seungjin-yang:GEM-Offline-DQM-Efficiency-Update__from-CMSSW_12_3_0_pre5
git clone https://github.com/seungjin-yang/GEMDQMUtils.git
scram setup nvidia-drivers
scram b distclean && scram b vclean && scram b clean
scram b -j 8
```

