```yaml
dataset: "/ExpressPhysics/Run2022D-Express-v2/FEVT"
run: 357902
oms: https://cmsoms.cern.ch/cms/runs/report?cms_run=357902
express_config: https://cmsweb.cern.ch/t0wmadatasvc/prod/express_config?run=357902
reco_config: https://cmsweb.cern.ch/t0wmadatasvc/prod/reco_config?run=357902
```

dqmio: https://cmsweb.cern.ch/dqm/offline/data/browse/ROOT/OfflineData/Run2022/Muon/0003579xx/DQM_V0001_R000357902__Muon__Run2022D-PromptReco-v2__DQMIO.root
dqm_gui: https://cmsweb.cern.ch/dqm/offline/start?runnr=357902;sampletype=offline_data;workspace=GEM;dataset=/Muon/Run2022D-PromptReco-v2/DQMIO



### submit
```zsh
module load lxbatch/spool
condor_submit -spool lxplus.condor
module unload lxbatch/spool
```
