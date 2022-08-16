#!/usr/bin/env python3
from pathlib import Path
import argparse
import ROOT
# import cppyy
from DataFormats.FWLite import Events # type: ignore
from DataFormats.FWLite import Handle # type: ignore

ROOT.gROOT.SetBatch() # type: ignore

class EDMObject:

    def __init__(self,
                 type: str,
                 module: str,
                 product_instance: str = '',
                 process: str = '') -> None:
        self._handle = Handle(type)
        self._label = [module, product_instance, process]

        self._product = None
        self._objs = []

    def get(self, event):
        event.getByLabel(self._label, self._handle)
        return self._handle.product()

    def init(self, event):
        self._product = self.get(event)
        self._objs = [each for each in self._product]

    def __call__(self, *args, **kwargs):
        return self.init(*args, **kwargs)

    def __iter__(self):
        return iter(self._objs)

    def __len__(self):
        return len(self._objs)

    def __getitem__(self, index):
        return self._objs[index]

    @property
    def product(self):
        return self._product

def convert_gem_id_to_str(gem_id):
    region = gem_id.region()
    station = gem_id.station()
    layer = gem_id.layer()
    chamber = gem_id.chamber()
    ieta = gem_id.ieta()
    return f'GEMDetId({region=}, {station=}, {layer=}, {chamber=}, {ieta=})'

def print_gem_id(gem_id):
    print(convert_gem_id_to_str(gem_id))


def analyze_gemcsc_segment(gemcsc_segment):
    csc_id = gemcsc_segment.cscDetId()
    if not csc_id.isME21():
        return False

    gem_hit_vec = gemcsc_segment.gemRecHits()
    print(f'# of GEM hits={gem_hit_vec.size()}')
    for gem_hit in gem_hit_vec:
        gem_id = gem_hit.gemId()
        print_gem_id(gem_id)

    return True


def run(input_path):
    """TODO: Docstring for main.

    :input_path: Path
    :returns: None

    """
    events = Events(f'file:{input_path}')

    gemcscsegment_vec = EDMObject(
        type='edm::RangeMap<CSCDetId,edm::OwnVector<GEMCSCSegment,edm::ClonePolicy<GEMCSCSegment> >,edm::ClonePolicy<GEMCSCSegment> >',
        module='gemcscSegments')

    obj_list = [
        gemcscsegment_vec,
    ]

    evt = next(iter(events))

    for obj in obj_list:
        obj(evt)

    for gemcsc_segment in gemcscsegment_vec:
        found_me21 = analyze_gemcsc_segment(gemcsc_segment)
        if found_me21:
            print('-' * 80)



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input-path", default=Path, required=True, help="input path")
    args = parser.parse_args()

    run(**vars(args))


if __name__ == "__main__":
    main()
