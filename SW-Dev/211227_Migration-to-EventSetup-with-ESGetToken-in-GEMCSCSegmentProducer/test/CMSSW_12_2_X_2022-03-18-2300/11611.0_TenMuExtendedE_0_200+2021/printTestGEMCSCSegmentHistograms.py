import uproot

path = './TestGEMCSCSegmentHistograms.root'
root_file = uproot.open(path)
for key in root_file.keys():
    obj = root_file[key]
    if hasattr(obj, 'to_hist'):
        hist = obj.to_hist()
        if hist.values().sum() == 0:
            print(f'{key} is empty')
        else:
            print(key)
            print(hist, end='\n' * 2)
    else:
        print(f'{key} is an instance of {type(obj)}, no \'to_hist\' method')
