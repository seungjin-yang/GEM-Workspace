#include "DataFormats/FWLite/interface/Handle.h" 

{
  gSystem->Load("libFWCoreFWLite.so"); 
  AutoLibraryLoader::enable();
  gSystem->Load("libDataFormatsFWLite.so");


  /*
  gSystem->Load("libDataFormatsFWLite.so");
  gSystem->Load("libSimDataFormatsGEMDigiSimLink.so");
  gSystem->Load("libDataFormatsCommon.so");
  */

  const TString input_path = "/store/user/seyang/GEM/220118_Update-GEMEfficiencyAnalyzer/CMSSW_12_3_0_pre5/UndergroundCosmicMuME11At0T+2021/step2_DIGI_L1_DIGI2RAW_HLT/step2_0.root";

  TFile root_file(input_path);
  fwlite::Event event(&root_file);

  for (event.toBegin(); ! event.atEnd(); ++event) {
    fwlite::Handle<edm::DetSetVector<GEMDigiSimLink> > objs;
    objs.getByLabel(event, "simMuonGEMDigis");
    break;
   }


}
