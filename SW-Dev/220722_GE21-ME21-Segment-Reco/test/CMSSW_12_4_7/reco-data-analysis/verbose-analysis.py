#!/usr/bin/env python3
from __future__ import annotations
from dataclasses import dataclass
import dataclasses
from pathlib import Path
import ROOT # type: ignore
from DataFormats.FWLite import Events # type: ignore
from GEMDQMUtils.Utils.fwlite import EDMObject # type: ignore

ROOT.gROOT.SetBatch()

@dataclass
class GEMDetId:
    region: int
    ring: int
    station: int
    layer: int
    chamber: int
    ieta: int

    @classmethod
    def from_cmssw(cls, gem_id) -> GEMDetId:
        kwargs: dict[str, int] = {field.name: getattr(gem_id, field.name)() for field in dataclasses.fields(cls)}
        return cls(**kwargs)

data_dir = Path('/eos/user/s/seyang/store/GEM/SW-Dev/220722_GE21-ME21-Segment-Reco/test/CMSSW_12_4_7/reco-data')

# input_files = list(map(lambda each: f'file:{each}', data_dir.glob('*.root')))
input_files = 'file:../reco-data/output_numEvent10.root'

event_loader = Events(input_files)


gem_csc_segment_range_map = EDMObject(
    type="edm::RangeMap<CSCDetId,edm::OwnVector<GEMCSCSegment,edm::ClonePolicy<GEMCSCSegment> >,edm::ClonePolicy<GEMCSCSegment> >",
    module="gemcscSegments")

obj_list = [
    gem_csc_segment_range_map,
]

for event in event_loader:
    for obj in obj_list:
        obj.init(event)

    event_number = event.eventAuxiliary().event()
    run_number = event.eventAuxiliary().run()
    print(f'{run_number=}, {event_number=}')
    for segment_idx, gem_csc_segment in enumerate(gem_csc_segment_range_map):
        gem_hit_size = gem_csc_segment.gemRecHits().size()
        print(f'\t{segment_idx=:d}: {gem_hit_size=:d}')
        for hit_idx, gem_hit in enumerate(gem_csc_segment.gemRecHits()):
            gem_id = GEMDetId.from_cmssw(gem_hit.gemId())
            print(f'\t\t{hit_idx=}: {gem_id}')
