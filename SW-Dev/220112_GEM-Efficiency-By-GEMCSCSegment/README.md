# Online GE1/1 Efficiency Monitoring with GEMCSCSegment
## Description
`TODO`

## Setup
```bash
CMSSW_VERSION=CMSSW_12_3_X_2022-01-16-0000
SCRAM_ARCH=slc7_amd64_gcc900 cmsrel ${CMSSW_VERSION}
cd ${CMSSW_VERSION}/src
cmsenv
git-cms-addpkg DQM/GEM
git-cms-addpkg DQM/Integration
git clone https://github.com/seungjin-yang/GEMDQMUtils.git
scram b -j 8
```

