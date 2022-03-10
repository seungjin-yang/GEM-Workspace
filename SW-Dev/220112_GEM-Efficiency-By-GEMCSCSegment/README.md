# Online GE1/1 Efficiency Monitoring with GEMCSCSegment
## Description
`TODO`

## Setup
```bash
source /cvmfs/cms.cern.ch/cmsset_default.sh
SCRAM_ARCH=slc7_amd64_gcc900 cmsrel CMSSW_12_3_0_pre5
cd CMSSW_12_3_0_pre5/src
cmsenv
git-cms-addpkg DQM/GEM
git-cms-addpkg DQM/Integration
git clone https://github.com/seungjin-yang/GEMDQMUtils.git
scram setup nvidia-drivers
cmsenv
scram b distclean && scram b vclean && scram b clean
scram b -j 8
```

## Sample
- https://cms-pdmv.cern.ch/relval/relvals?prepid=CMSSW_12_3_0_pre5__fullsim_PU_2021_14TeV-ZMM_14-00002&shown=1023&page=0&limit=50
    - https://cms-pdmv.cern.ch/relval/relvals?output_dataset=/RelValZMM_14/CMSSW_12_3_0_pre5-123X_mcRun3_2021_realistic_v6-v1/GEN-SIM&shown=1023&page=0&limit=50
    - https://github.com/cms-sw/cmssw/blob/CMSSW_12_3_0_pre5/Configuration/Generator/python/ZMM_14TeV_TuneCP5_cfi.py


## PRs
- PR to master (12_3_X): [Add GE1/1 detection efficiency monitor using GEMCSCSegment #37178](https://github.com/cms-sw/cmssw/pull/37178)
