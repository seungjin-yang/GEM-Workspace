#!/bin/bash -ex
XDIR=$(/bin/pwd)
export SCRAM_ARCH=slc7_amd64_gcc10
if [ -e 'CMSSW_12_3_X_2022-03-08-1100' ] ; then echo 'There is already CMSSW_12_3_X_2022-03-08-1100 dev area. Please cleanup or run $0 in a clean directory' ; fi
tar -xzf /cvmfs/cms-ci.cern.ch/week1/cms-sw/cmssw/37178/22948/cmssw.tar.gz
cd CMSSW_12_3_X_2022-03-08-1100
SCRAM_VER=$(cat config/scram_version)
EXT=pl
SCRAM_HOME_BASE=src
if [ $(echo ${SCRAM_VER} | grep '^V3' | wc -l) -gt 0 ] ; then EXT=py ; SCRAM_HOME_BASE=''; fi
export SCRAM_TOOL_HOME=/cvmfs/cms-ib.cern.ch/week1/share/lcg/SCRAMV1/${SCRAM_VER}/${SCRAM_HOME_BASE}
./config/SCRAM/projectAreaRename.${EXT} /data/cmsbld/jenkins/workspace/ib-run-pr-tests ${XDIR} slc7_amd64_gcc10
./config/SCRAM/linkexternal.${EXT} --arch slc7_amd64_gcc10
find config/SCRAM -name __pycache__ -type d | xargs --no-run-if-empty rm -rf
