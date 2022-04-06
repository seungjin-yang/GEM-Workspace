from collections import Counter
import tqdm
import ROOT
from DataFormats.FWLite import Events
from DataFormats.FWLite import Handle

path = "/store/user/seyang/GEM/220118_Update-GEMEfficiencyAnalyzer/CMSSW_12_3_0_pre5/UndergroundCosmicMuME11At0T+2021/step2_DIGI_L1_DIGI2RAW_HLT/step2_0.root"
root_file = ROOT.TFile(path)
tree = root_file.Events
# tree.Print()

num_entries = tree.GetEntries()
pbar = tqdm.tqdm(tree, total=num_entries)

data = []
for event in pbar:
    link_set_vector = event.GEMDigiSimLinkedmDetSetVector_simMuonGEMDigis_GEM_HLT.product()
    print(link_set_vector)
    print(dir(link_set_vector))
    print(len(link_set_vector))
    break
