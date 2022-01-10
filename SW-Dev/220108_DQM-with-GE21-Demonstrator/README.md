# 220108_DQM-with-GE21-Demonstrator

## Description
`TODO`


## Reproducing
```bash
scram project -n 2022.01.07.ge21.sunanda.changes.test CMSSW CMSSW_12_3_X_2022-01-06-2300
cd 2022.01.07.ge21.sunanda.changes.test/src
cmsenv
git cms-merge-topic watson-ij:ge21-demonstrator-gemgeobuilder
git cms-merge-topic bsunanda:Run3-gex108
git cms-addpkg DQM/GEM
USER_CXXFLAGS="-g" scram b -j16  -k
runTheMatrix.py -w upgrade -l 11634.911
```

```txt
$ runTheMatrix.py -w upgrade -l 11634.911
#5  GEMChamber::id (this=0x0) at /cms/ldap_home/slowmoyang/Projects/GEM/SW-Dev/220108_DQM-with-GE21-Demonstrator/test/reproducing/2022.01.07.ge21.sunanda.changes.test/src/Geometry/GEMGeometry/src/GEMChamber.cc:17
#6  0x00007f180a63e22c in GEMDQMBase::loadChambers (this=this@entry=0x7f180bf2ac00) at /cms/ldap_home/slowmoyang/Projects/GEM/SW-Dev/220108_DQM-with-GE21-Demonstrator/test/reproducing/2022.01.07.ge21.sunanda.chan
ges.test/src/DQM/GEM/src/GEMDQMBase.cc:56
#7  0x00007f180a6c726d in GEMRecHitSource::bookHistograms (this=0x7f180bf2ac00, ibooker=..., iSetup=...) at /cms/ldap_home/slowmoyang/Projects/GEM/SW-Dev/220108_DQM-with-GE21-Demonstrator/test/reproducing/2022.01
.07.ge21.sunanda.changes.test/src/DQM/GEM/plugins/GEMRecHitSource.cc:35
#8  0x00007f180a69193a in DQMEDAnalyzer::beginRun(edm::Run const&, edm::EventSetup const&)::{lambda(dqm::implementation::IBooker&)#1}::operator()(dqm::implementation::IBooker&) const (booker=..., __closure=<synth
etic pointer>) at /cvmfs/cms-ib.cern.ch/week0/slc7_amd64_gcc10/cms/cmssw-patch/CMSSW_12_3_X_2022-01-06-2300/src/DQMServices/Core/interface/DQMEDAnalyzer.h:87
```


## Setup
```bash
SCRAM_ARCH=slc7_amd64_gcc900 cmsrel CMSSW_12_3_X_2022-01-06-2300
cd CMSSW_12_3_X_2022-01-06-2300/src
cmsenv
git cms-merge-topic watson-ij:ge21-demonstrator-gemgeobuilder
git cms-merge-topic bsunanda:Run3-gex108
git cms-merge-topic seungjin-yang:Moving-GEM-Offline-DQM__from-CMSSW_12_3_0_pre2
USER_CXXFLAGS="-g" scram b -j16  -k
```
