# CMSSW_12_2_0_2021vsCMSSW_12_2_0_pre3_2021
## Description

- https://cms-pdmv.cern.ch/relmon/1643045342___CMSSW_12_2_0_2021vsCMSSW_12_2_0_pre3_2021/FullSimReport/RelValSingleMuPt10_122X_mcRun3_2021_realistic_v5/6dc6bd0fcc.html
- https://cmssdt.cern.ch/SDT/ReleaseNotes/CMSSW_12/CMSSW_12_2_0.html


root://eoscms.cern.ch//eos/cms/

### Reference (CMSSW_12_2_0_pre3_2021)
- DQMIO: https://cmsweb.cern.ch/dqm/relval/data/browse/ROOT/RelVal/CMSSW_12_2_x/DQM_V0001_R000000001__RelValSingleMuPt10__CMSSW_12_2_0_pre3-122X_mcRun3_2021_realistic_v5-v1__DQMIO.root

```console
$ dasgoclient -query="/RelValSingleMuPt10/CMSSW_12_2_0_pre3-122X_mcRun3_2021_realistic_v5-v1/*"
/RelValSingleMuPt10/CMSSW_12_2_0_pre3-122X_mcRun3_2021_realistic_v5-v1/DQMIO
/RelValSingleMuPt10/CMSSW_12_2_0_pre3-122X_mcRun3_2021_realistic_v5-v1/GEN-SIM
/RelValSingleMuPt10/CMSSW_12_2_0_pre3-122X_mcRun3_2021_realistic_v5-v1/GEN-SIM-DIGI-RAW
/RelValSingleMuPt10/CMSSW_12_2_0_pre3-122X_mcRun3_2021_realistic_v5-v1/GEN-SIM-RECO
/RelValSingleMuPt10/CMSSW_12_2_0_pre3-122X_mcRun3_2021_realistic_v5-v1/MINIAODSIM
/RelValSingleMuPt10/CMSSW_12_2_0_pre3-122X_mcRun3_2021_realistic_v5-v1/NANOAODSIM

$ dasgoclient -query="file dataset=/RelValSingleMuPt10/CMSSW_12_2_0_pre3-122X_mcRun3_2021_realistic_v5-v1/GEN-SIM-DIGI-RAW"
/store/relval/CMSSW_12_2_0_pre3/RelValSingleMuPt10/GEN-SIM-DIGI-RAW/122X_mcRun3_2021_realistic_v5-v1/2580000/f3c5aa14-0d1d-4130-96fc-b5206d65d707.root
/store/relval/CMSSW_12_2_0_pre3/RelValSingleMuPt10/GEN-SIM-DIGI-RAW/122X_mcRun3_2021_realistic_v5-v1/2580000/0e7ff673-5642-4bdf-b079-407797c633a6.root

$ dasgoclient -query="file dataset=/RelValSingleMuPt10/CMSSW_12_2_0_pre3-122X_mcRun3_2021_realistic_v5-v1/GEN-SIM-RECO"
/store/relval/CMSSW_12_2_0_pre3/RelValSingleMuPt10/GEN-SIM-RECO/122X_mcRun3_2021_realistic_v5-v1/2580000/34cdec96-f48d-457c-a51b-82ad6ccd8903.root

$ OUTPUT_DIR=/store/scratch/seyang//relval/CMSSW_12_2_0_pre3/RelValSingleMuPt10/GEN-SIM-RECO/122X_mcRun3_2021_realistic_v5-v1/2580000/
$ mkdir -vp ${OUTPUT_DIR}
$ xrdcp -v root://eoscms.cern.ch//eos/cms/store/relval/CMSSW_12_2_0_pre3/RelValSingleMuPt10/GEN-SIM-RECO/122X_mcRun3_2021_realistic_v5-v1/2580000/34cdec96-f48d-457c-a51b-82ad6ccd8903.root ${OUTPUT_DIR}
```

### Test (CMSSW_12_2_0_2021)

- DQMIO: https://cmsweb.cern.ch/dqm/relval/data/browse/ROOT/RelVal/CMSSW_12_2_x/DQM_V0001_R000000001__RelValSingleMuPt10__CMSSW_12_2_0-122X_mcRun3_2021_realistic_v5-v2__DQMIO.root
- RelVal: https://cms-pdmv.cern.ch/relval/relvals?prepid=CMSSW_12_2_0_pre3__fullsim_noPU_2021_14TeV-SingleMuPt10-00003&shown=1023&page=0&limit=50

```console
$ dasgoclient -query="/RelValSingleMuPt10/CMSSW_12_2_0-122X_mcRun3_2021_realistic_v5-v2/*"
/RelValSingleMuPt10/CMSSW_12_2_0-122X_mcRun3_2021_realistic_v5-v2/DQMIO
/RelValSingleMuPt10/CMSSW_12_2_0-122X_mcRun3_2021_realistic_v5-v2/GEN-SIM-DIGI-RAW
/RelValSingleMuPt10/CMSSW_12_2_0-122X_mcRun3_2021_realistic_v5-v2/GEN-SIM-RECO
/RelValSingleMuPt10/CMSSW_12_2_0-122X_mcRun3_2021_realistic_v5-v2/MINIAODSIM
/RelValSingleMuPt10/CMSSW_12_2_0-122X_mcRun3_2021_realistic_v5-v2/NANOAODSIM

$ dasgoclient -query="file dataset=/RelValSingleMuPt10/CMSSW_12_2_0-122X_mcRun3_2021_realistic_v5-v2/GEN-SIM-RECO"
/store/relval/CMSSW_12_2_0/RelValSingleMuPt10/GEN-SIM-RECO/122X_mcRun3_2021_realistic_v5-v2/2580000/209d62dd-6b03-4fa9-8b4d-5dd03957e0a8.root

$ xrdcp -v root://eoscms.cern.ch//eos/cms/store/relval/CMSSW_12_2_0/RelValSingleMuPt10/GEN-SIM-RECO/122X_mcRun3_2021_realistic_v5-v2/2580000/209d62dd-6b03-4fa9-8b4d-5dd03957e0a8.root /store/scratch/seyang/relval/CMSSW_12_2_0/RelValSingleMuPt10/GEN-SIM-RECO/122X_mcRun3_2021_realistic_v5-v2/2580000
```

- /store/scratch/seyang/relval/CMSSW_12_2_0/RelValSingleMuPt10/GEN-SIM-RECO/122X_mcRun3_2021_realistic_v5-v2/2580000

