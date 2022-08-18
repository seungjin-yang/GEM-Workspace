# GE2/1-ME2/1 Segment Reconstruction
## Description

## Recipe
### Init
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

### Test1
- [/RelValZMM_14/CMSSW_12_5_0_pre4-PU_124X_mcRun3_2022_realistic_v10_RECOonly-v2/GEN-SIM-RECO](https://cms-pdmv.cern.ch/relval/relvals?prepid=CMSSW_12_5_0_pre4__AUTOMATED_fullsim_PU_2022_14TeV_RECOonly-ZMM_14-00002)
```bash
dasgoclient -query="/RelVal*/*12_5_0_pre4*/GEN-SIM-RECO"

```
