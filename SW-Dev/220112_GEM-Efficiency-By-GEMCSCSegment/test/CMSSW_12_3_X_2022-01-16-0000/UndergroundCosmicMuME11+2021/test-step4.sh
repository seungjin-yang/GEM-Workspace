CFG=step4_DQM.py
INPUT_FILE=/xrootd/store/user/seyang/GEM/220101_GEM-Efficiency-By-GEMCSCSegment/CMSSW_12_3_0_pre2/UndergroundCosmicMuME11_2021/step3_RAW2DIGI_L1Reco_RECO/step3_0.root
FILE_PREPEND=file:

LOG_FILE=logs/test-step4.txt

cmsRun ${CFG} inputFiles=${INPUT_FILE} filePrepend=${FILE_PREPEND} > ${LOG_FILE} 2>&1 &
tail -f ${LOG_FILE}
