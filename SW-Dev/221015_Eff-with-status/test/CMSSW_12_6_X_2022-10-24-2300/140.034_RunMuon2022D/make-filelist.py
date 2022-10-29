#!/usr/bin/env python
from pathlib import Path

data_dir = '/eos/user/s/seyang/store/GEM/step2/'
data_dir = Path(data_dir)

for each in data_dir.glob('*.root'):
    print(each)
