- https://cmsoms.cern.ch/cms/runs/report?cms_run=357801
- https://cmsweb.cern.ch/dqm/offline/start?runnr=357801;sampletype=offline_data;workspace=GEM;dataset=/StreamExpress/Run2022B-Express-v1/DQMIO
- https://cmsweb.cern.ch/t0wmadatasvc/prod/express_config?run=357801
- https://github.com/dmwm/T0/blob/f6c2c9a/etc/ProdOfflineConfiguration.py


```console
$ dasgoclient -query="file dataset=/Muon/Run2022C-v1/RAW run=357801"
$ dasgoclient -query="file dataset=/Muon/Run2022C-v1/RAW run=357801" | head -n 1
/store/data/Run2022C/Muon/RAW/v1/000/357/442/00000/ede3683c-0a20-495c-9e70-df0958fa2256.root
$ dasgoclient -query="site file=/store/data/Run2022C/Muon/RAW/v1/000/357/442/00000/ede3683c-0a20-495c-9e70-df0958fa2256.root"
T0_CH_CERN_Disk
```

```python
defaultCMSSWVersion = {
    'default': "CMSSW_12_4_6"
}
ppScenario = "ppEra_Run3"
expressGlobalTag = "124X_dataRun3_Express_v5"
promptrecoGlobalTag = "124X_dataRun3_Prompt_v4"
globalTagConnect = "frontier://PromptProd/CMS_CONDITIONS"
```

```bash
python3 ${CMSSW_RELEASE_BASE}/src/Configuration/DataProcessing/test/RunPromptReco.py \
    --scenario=ppEra_Run3 \
    --global-tag=124X_dataRun3_Prompt_v4 \
    --reco \
    --lfn /store/whatever
```


```console
$ dasgoclient -query="dataset run=357081" | rg FEVT
/ExpressPhysics/Run2022C-Express-v1/FEVT
/HLTMonitor/Run2022C-Express-v1/FEVTHLTALL
$ dasgoclient -query="file dataset=/ExpressPhysics/Run2022C-Express-v1/FEVT run=357081" | head -n 1
/store/express/Run2022C/ExpressPhysics/FEVT/Express-v1/000/357/081/00000/c196bc27-4ebd-4c37-99f1-79429f16af26.root
$ dasgoclient -query="site file=/store/express/Run2022C/ExpressPhysics/FEVT/Express-v1/000/357/081/00000/c196bc27-4ebd-4c37-99f1-79429f16af26.root"
T0_CH_CERN_Disk
T2_CH_CERN
$ cms-get-site.py T2_CH_CERN -p XRootD
{
    "protocol": "XRootD",
    "access": "global-rw",
    "prefix": "root://eoscms.cern.ch//eos/cms"
}
$ xrdcp -v root://eoscms.cern.ch//eos/cms//store/express/Run2022C/ExpressPhysics/FEVT/Express-v1/000/357/081/00000/c196bc27-4ebd-4c37-99f1-79429f16af26.root .
```
