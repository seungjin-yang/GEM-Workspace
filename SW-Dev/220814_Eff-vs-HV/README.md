# Detection Efficiency vs HV

## Recipe
### Setup
```bash
source /cvmfs/cms.cern.ch/cmsset_default.sh
CMSSW_VERSION=CMSSW_12_5_0_pre4
cmsrel ${CMSSW_VERSION}
cd ${CMSSW_VERSION}/src
eval `scramv1 runtime -sh`
git-cms-addpkg DQM/GEM
```

```bash
dasgoclient --query "/SingleMuon/Run2022*-v1/RAW"
dasgoclient -query "run dataset=/SingleMuon/Run2022C-v1/RAW"
```

###

https://cmsweb.cern.ch/dqm/offline/start?runnr=355100;sampletype=offline_data;workspace=GEM;dataset=/StreamExpress/Run2022B-Express-v1/DQMIO



```bash
/afs/cern.ch/user/f/fivone/public/HV_Fetch_Data/DCS_Fetcher
python GEMDCSP5Monitor.pyc 2022-04-01_15:22:31 2022-04-02_15:22:31 HV 0 -c all
```

## Reference
1. https://github.com/cms-sw/cmssw/pull/35335
2. https://github.com/cms-sw/cmssw/blob/CMSSW_12_5_0_pre4/DQMServices/Components/plugins/DQMProvInfo.cc#L498-L499
