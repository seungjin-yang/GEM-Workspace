# GE2/1-ME2/1 Segment Reconstruction
## Description

## Recipe
### Setup
```bash
source /cvmfs/cms.cern.ch/cmsset_default.sh
CMSSW_VERSION=CMSSW_12_5_0_pre4
cmsrel ${CMSSW_VERSION}
cd ${CMSSW_VERSION}/src
# eval `scramv1 runtime -sh`
cmsenv
git-cms-addpkg RecoLocalMuon/GEMCSCSegment
git-cms-addpkg DQM/GEM
git-cms-addpkg DQM/Integration
```
