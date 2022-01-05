## Description
Got [an exception](https://github.com/cms-sw/cmssw/blob/master/FWCore/Framework/src/EventSetupRecord.cc#L134-L140) while running step3 with GEMCSCSegment reco. Need to fix [GEMCSCSegmentProducer](https://github.com/cms-sw/cmssw/blob/master/RecoLocalMuon/GEMCSCSegment/plugins/GEMCSCSegmentProducer.cc#L39-L46), which still uses a deprecated pattern when loading geometry. 

* step3_RAW2DIGI_L1Reco_RECO.py
```python
# Path and EndPath definitions
process.load('RecoLocalMuon.GEMCSCSegment.gemcscSegments_cfi')
process.gemcscSegments_step = cms.Path(process.gemcscSegments)

process.raw2digi_step = cms.Path(process.RawToDigi)
process.L1Reco_step = cms.Path(process.L1Reco)
process.reconstruction_step = cms.Path(process.reconstructionCosmics)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.FEVToutput_step = cms.EndPath(process.FEVToutput)

# Schedule definition
process.schedule = cms.Schedule(
    process.raw2digi_step,
    process.L1Reco_step,
    process.reconstruction_step,
    process.gemcscSegments_step,
    process.endjob_step,
    process.FEVToutput_step
)
```

```console
$ cmsRun step3_RAW2DIGI_L1Reco_RECO.py
----- Begin Fatal Exception 27-Dec-2021 19:16:27 KST-----------------------
An exception of category 'MustUseESGetToken' occurred while
   [0] Processing  Event run: 1 lumi: 1 event: 221 stream: 0
   [1] Running path 'gemcscSegments_step'
   [2] Calling method for module GEMCSCSegmentProducer/'gemcscSegments'
Exception Message:
Called EventSetupRecord::get without using a ESGetToken.
 While requesting data type:CSCGeometry label:''
See https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideHowToGetDataFromES
for instructions how to migrate the calling code
----- End Fatal Exception -------------------------------------------------
```

## Setup
```bash
SCRAM_ARCH=slc7_amd64_gcc900 cmsrel CMSSW_12_3_0_pre2
cd CMSSW_12_3_0_pre2/src
eval `scramv1 runtime -sh`
# git-cms-addpkg RecoLocalMuon/GEMCSCSegment
git-cms-merge-topic seungjin-yang:Fix-GEMCSCSegmentProducer-Geometry-Loading__from-CMSSW_12_3_0_pre2
```

## Test
[CMSSW_12_3_0_pre2__fullsim_PU_2021_14TeV-ZMM_14-00001](https://cms-pdmv.cern.ch/relval/relvals?prepid=CMSSW_12_3_0_pre2__fullsim_PU_2021_14TeV-ZMM_14-00001&shown=1023&page=0&limit=50)

```console
$ cd test
$ DATASET="/RelValZMM_14/CMSSW_12_3_0_pre2-122X_mcRun3_2021_realistic_v5-v1/GEN-SIM-DIGI-RAW"
$ dasgoclient -query "file dataset=${DATASET}" > filelist-2021-ZMM-step2.txt
$ TESTFILE=$(head -n 1 filelist.txt) 
$ dasgoclient -query="site file=${TESTFILE}"
T2_CH_CERN
T2_IN_TIFR
$ grep -z xrootd /cvmfs/cms.cern.ch/SITECONF/T2_CH_CERN/PhEDEx/storage.xml
  <!-- Map any LFN with /store/ to xrootd on EOS -->
  <lfn-to-pfn protocol="eos"
    path-match="/+store/(.*)"
    result="root://eoscms.cern.ch//eos/cms/store/$1"/>
$ bash produce.sh 
$ bash analyze.sh
```
Then, check `plotting.ipynb`

## NOTE
- When running `TestGEMCSCSegmentAnalyzer`, got a lot of err msgs like `Error in <TROOT::WriteTObject>: The current directory (root) is not associated with a file. The object (yGEMPool_odd_newE_simhit) has not been written.`, where `yGEMPool_odd_newE_simhit` is the name of the histogram.

## Result
- Branch: [seungjin-yang:Fix-GEMCSCSegmentProducer-Geometry-Loading__from-CMSSW_12_3_0_pre2](https://github.com/seungjin-yang/cmssw/tree/Fix-GEMCSCSegmentProducer-Geometry-Loading__from-CMSSW_12_3_0_pre2)
- PR: [Fix gemcsc segment producer geometry loading from cmssw 12 3 0 pre2 #36628](https://github.com/cms-sw/cmssw/pull/36628)
