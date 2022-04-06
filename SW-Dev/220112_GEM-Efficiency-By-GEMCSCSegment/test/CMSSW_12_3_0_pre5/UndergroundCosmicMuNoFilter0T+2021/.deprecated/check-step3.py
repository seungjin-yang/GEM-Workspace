#!/usr/bin/env python3
import argparse
from pathlib import Path
from collections import Counter
import tqdm
import ROOT
from DataFormats.FWLite import Events
from DataFormats.FWLite import Handle


parser = argparse.ArgumentParser()
parser.add_argument("input_path", type=Path)
parser.add_argument('-b', '--branch', action='store_true')
args = parser.parse_args()

if not args.input_path.exists():
    raise FileNotFoundError

root_file = ROOT.TFile(str(args.input_path))
tree = root_file.Events

if args.branch:
    tree.Print()
else:
    num_entries = tree.GetEntries()
    pbar = tqdm.tqdm(tree, total=num_entries)

    data = []
    for event in pbar:
        gemcsc_segment_collection = event.CSCDetIdGEMCSCSegmentsOwnedRangeMap_gemcscSegments__RECO.product()
        for idx, each in enumerate(gemcsc_segment_collection.begin()):
            print(idx)
        break
