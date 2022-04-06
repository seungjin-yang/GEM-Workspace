source setup.sh
rm -vf filelist-step4_DQM.txt
gem-dqm-make-file-list.py  /store/user/seyang/GEM/220112_GEM-Efficiency-By-GEMCSCSegment/CMSSW_12_3_0_pre5/UndergroundCosmicMuME11At0T+2021/step4_DQM
wc -l filelist-step4_DQM.txt
