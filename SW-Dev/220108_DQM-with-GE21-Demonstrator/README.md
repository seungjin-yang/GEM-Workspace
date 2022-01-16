# 220108_DQM-with-GE21-Demonstrator

## Description
`TODO`


## Reproducing
```bash
SCRAM_ARCH=slc7_amd64_gcc900 scram project -n 2022.01.07.ge21.sunanda.changes.test CMSSW CMSSW_12_3_X_2022-01-06-2300
cd 2022.01.07.ge21.sunanda.changes.test/src
cmsenv
git cms-merge-topic watson-ij:ge21-demonstrator-gemgeobuilder
git cms-merge-topic bsunanda:Run3-gex108
git cms-addpkg DQM/GEM
USER_CXXFLAGS="-g -DDEBUG" scram b -j16 -k
runTheMatrix.py -w upgrade -l 11634.911
```

```txt
$ runTheMatrix.py -w upgrade -l 11634.911
%MSG-w MonitorElement:   GEMEfficiencyAnalyzer:gemEfficiencyAnalyzerSta@streamBeginRun  10-Jan-2022 14:46:18 KST Run: 1 Stream: 0
*** MonitorElement: WARNING:setBinLabel: attempting to set label of non-existent bin number for ME: GEM/Efficiency/type2/Efficiency/detector_GE21-P-L2

%MSG
%MSG-w MonitorElement:   GEMEfficiencyAnalyzer:gemEfficiencyAnalyzerTightGlb@streamBeginRun  10-Jan-2022 14:46:18 KST Run: 1 Stream: 0
*** MonitorElement: WARNING:setBinLabel: attempting to set label of non-existent bin number for ME: GEM/Efficiency/type1/Efficiency/detector_GE21-P-L2

%MSG

#5  GEMChamber::id (this=0x0) at /cms/ldap_home/slowmoyang/Projects/GEM/SW-Dev/220108_DQM-with-GE21-Demonstrator/reproducing/2022.01.07.ge21.sunanda.changes.test/src/Geometry/GEMGeometry/src/GEMChamber.cc:17
#6  0x00007fdce2d03f8c in GEMDQMBase::loadChambers (this=this@entry=0x7fdce4708c00) at /cms/ldap_home/slowmoyang/Projects/GEM/SW-Dev/220108_DQM-with-GE21-Demonstrator/reproducing/2022.01.07.ge21.sunanda.changes.test/src/DQM/GEM/src/GEMDQMBase.cc:56
#7  0x00007fdce2d55a4d in GEMRecHitSource::bookHistograms (this=0x7fdce4708c00, ibooker=..., iSetup=...) at /cms/ldap_home/slowmoyang/Projects/GEM/SW-Dev/220108_DQM-with-GE21-Demonstrator/reproducing/2022.01.07.ge21.sunanda.changes.test/src/DQM/GEM/plugins/GEMRecHitSource.cc:35
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
