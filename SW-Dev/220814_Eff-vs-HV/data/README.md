- https://cmsoms.cern.ch/cms/runs/report?cms_run=357442
- https://cmsweb.cern.ch/dqm/offline/start?runnr=357442;sampletype=offline_data;workspace=GEM;dataset=/StreamExpress/Run2022B-Express-v1/DQMIO
- https://cmsweb.cern.ch/t0wmadatasvc/prod/express_config?run=357442
- https://github.com/dmwm/T0/blob/f6c2c9a/etc/ProdOfflineConfiguration.py


```console
$ dasgoclient -query="file dataset=/Muon/Run2022C-v1/RAW run=357442"
$ dasgoclient -query="file dataset=/Muon/Run2022C-v1/RAW run=357442" | head -n 1
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

