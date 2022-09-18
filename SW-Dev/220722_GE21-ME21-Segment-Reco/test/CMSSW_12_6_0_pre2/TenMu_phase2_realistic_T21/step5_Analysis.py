import FWCore.ParameterSet.Config as cms # type: ignore
from Configuration.Eras.Era_Run3_cff import Run3 # type: ignore
from Configuration.Eras.Era_Phase2C18I13M9_cff import Phase2C18I13M9 # type: ignore

process = cms.Process('Analysis', Phase2C18I13M9)

process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load('RecoLocalMuon.GEMCSCSegment.gemcscCoincidenceRateAnalyzer_cfi')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1),
    output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
)

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('file:step4.root'),
    secondaryFileNames = cms.untracked.vstring()
)

from Configuration.AlCa.GlobalTag import GlobalTag # type: ignore
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase2_realistic_T21', '')

process.TFileService = cms.Service("TFileService",
    fileName = cms.string('file:output.root')
)

process.gemcsc_step = cms.Path(process.gemcscCoincidenceRateAnalyzer)
process.schedule = cms.Schedule(process.gemcsc_step)
