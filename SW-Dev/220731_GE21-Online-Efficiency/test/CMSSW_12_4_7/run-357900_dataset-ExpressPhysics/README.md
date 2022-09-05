```yaml
run: 357900
dataset: "/ExpressPhysics/Run2022D-Express-v2/FEVT"
site: "T2_CH_CERN"
site_prefix: "root://eoscms.cern.ch//eos/cms"
```

```zsh
dasgoclient -query="dataset run=357900"
curl -k "https://cmsweb.cern.ch/t0wmadatasvc/prod/express_config?run=357900"
split -l 100 -d --additional-suffix .txt input-files.txt
```



### submit
```zsh
module load lxbatch/spool
condor_submit -spool lxplus.condor
module unload lxbatch/spool
```
