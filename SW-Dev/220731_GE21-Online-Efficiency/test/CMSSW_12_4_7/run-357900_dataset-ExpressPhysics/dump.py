import uproot
path = 'DQM_V0001_R000357900__Global__CMSSW_X_Y_Z__RECO.root'
root_file = uproot.open(path)
key = f'DQMData/Run 357900/GEM/Run summary/Efficiency/GEMCSCSegment'
for each in sorted(root_file[key].keys(recursive=False, cycle=False)):
    print(each)
