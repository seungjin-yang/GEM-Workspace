#!/usr/bin/env python3
import argparse
from pathlib import Path
import uproot

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('paths', type=Path, nargs='+')
    args = parser.parse_args()

    for path in args.paths:
        print(path)
        root_file = uproot.open(path)
        gem_dir = root_file['DQMData/Run 1/GEM/Run summary']
        for key in gem_dir.keys(recursive=False):
            sub_dir = gem_dir[key]
            count = len(sub_dir.keys(filter_classname=lambda classname: classname not in ['TDirectory']))
            print(f'\t - {key}: {count:d}')

if __name__ == '__main__':
    main()
