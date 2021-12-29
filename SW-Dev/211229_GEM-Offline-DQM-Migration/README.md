## Description


## Reproduce
`TODO`

## Setup
```bash
cmsrel CMSSW_12_3_0_pre2
cd CMSSW_12_3_0_pre2/src
eval `scramv1 runtime -sh`
git-cms-addpkg DQM/GEM DQMOffline/Muon DQMOffline/Configuration
```

```bash
find . -type f -name "*.h" -exec sed -i 's/DQMOffline_Muon_/DQM_GEM_/g' {} +
```

## Test
- [fullsim_noPU_2021_14TeV](https://cms-pdmv.cern.ch/relval/relvals?batch_name=fullsim_noPU_2021_14TeV&shown=1023&page=0&limit=50)
  - [CMSSW_12_3_0_pre2__fullsim_noPU_2021_14TeV-ZMM_14-00001](https://cms-pdmv.cern.ch/relval/relvals?prepid=CMSSW_12_3_0_pre2__fullsim_noPU_2021_14TeV-ZMM_14-00001&shown=1023&page=0&limit=50)

```console
$ dasgoclient -query="file dataset=/RelValZMM_14/CMSSW_12_3_0_pre2-122X_mcRun3_2021_realistic_v5-v1/DQMIO"
/store/relval/CMSSW_12_3_0_pre2/RelValZMM_14/DQMIO/122X_mcRun3_2021_realistic_v5-v1/2580000/F9181936-62C1-11EC-926B-97C18E80BEEF.root
$ TESTFILE=/store/relval/CMSSW_12_3_0_pre2/RelValZMM_14/DQMIO/122X_mcRun3_2021_realistic_v5-v1/2580000/F9181936-62C1-11EC-926B-97C18E80BEEF.root
$ dasgoclient -query="site file=${TESTFILE}"
T2_CH_CERN
T2_UK_London_IC
$ grep -z xrootd /cvmfs/cms.cern.ch/SITECONF/T2_CH_CERN/PhEDEx/storage.xml
  <!-- Map any LFN with /store/ to xrootd on EOS -->
  <lfn-to-pfn protocol="eos"
    path-match="/+store/(.*)"
    result="root://eoscms.cern.ch//eos/cms/store/$1"/>
$ xrdcp root://eoscms.cern.ch//eos/cms/${TESTFILE} .
```

