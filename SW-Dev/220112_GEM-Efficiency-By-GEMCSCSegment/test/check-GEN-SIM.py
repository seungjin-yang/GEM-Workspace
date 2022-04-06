from collections import Counter
import tqdm
import ROOT
from DataFormats.FWLite import Events
from DataFormats.FWLite import Handle

path = "/store/user/seyang/GEM/220112_GEM-Efficiency-By-GEMCSCSegment/CMSSW_12_3_0_pre5/UndergroundCosmicMuNoFilter0T+2021/step1_GEN_SIM/step1_101.root"
root_file = ROOT.TFile(path)

num_events = root_file.Events.GetEntries()
pbar = tqdm.tqdm(root_file.Events, total=num_events)

data = []
for event in pbar:
    num_muons = 0
    for gen_particle in event.recoGenParticles_genParticles__SIM.product():
        if gen_particle.status() != 1:
            continue
        if abs(gen_particle.pdgId()) != 13:
            continue
        num_muons += 1
    pbar.set_description(f'# of muons in the event = {num_muons}')
    data.append(num_muons)
data = Counter(data)
print(data)
