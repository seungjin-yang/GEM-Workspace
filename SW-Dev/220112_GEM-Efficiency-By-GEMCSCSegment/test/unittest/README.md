```bash
bash /cvmfs/cms-ci.cern.ch/week1/cms-sw/cmssw/37178/22948/install.sh
scram b -k -j 16  runtests
```

```txt
===== Test "TestDQMOnlineClient-gem_dqm_sourceclient" ====
+ [[ 1 -eq 0 ]]
+ [[ -z '' ]]
+ LOCAL_TEST_DIR=.
+ [[ -z '' ]]
+ CLIENTS_DIR=./src/DQM/Integration/python/clients
+ mkdir -p ./upload
+ cmsRun ./src/DQM/Integration/python/clients/gem_dqm_sourceclient-live_cfg.py unitTest=True
----- Begin Fatal Exception 10-Mar-2022 10:30:35 CET-----------------------
An exception of category 'ConfigFileReadError' occurred while
   [0] Processing the python configuration file named ./src/DQM/Integration/python/clients/gem_dqm_sourceclient-live_cfg.py
Exception Message:
 unknown python problem occurred.
IndexError: list index out of range

At:
  /afs/cern.ch/user/s/seyang/private/GEM-Workspace/SW-Dev/220112_GEM-Efficiency-By-GEMCSCSegment/test/unittest/CMSSW_12_3_X_2022-03-08-1100/python/DQM/Integration/config/unittestinputsource_cfi.py(99): <module>
  <frozen importlib._bootstrap>(228): _call_with_frames_removed
  <frozen importlib._bootstrap_external>(850): exec_module
  <frozen importlib._bootstrap>(695): _load_unlocked
  <frozen importlib._bootstrap>(986): _find_and_load_unlocked
  <frozen importlib._bootstrap>(1007): _find_and_load
  /cvmfs/cms-ib.cern.ch/week1/slc7_amd64_gcc10/cms/cmssw-patch/CMSSW_12_3_X_2022-03-08-1100/python/FWCore/ParameterSet/Config.py(722): load
  ./src/DQM/Integration/python/clients/gem_dqm_sourceclient-live_cfg.py(15): <module>

----- End Fatal Exception -------------------------------------------------

---> test TestDQMOnlineClient-gem_dqm_sourceclient had ERRORS
TestTime:211
^^^^ End Test TestDQMOnlineClient-gem_dqm_sourceclient ^^^^
```


https://cmssdt.cern.ch/jenkins/job/ib-run-pr-tests/22948/console
