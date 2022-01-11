# Modified from RecoLocalMuon/GEMCSCSegment/test/testgemcscsegmentanalyzer_cfg.py

import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Run3_cff import Run3

process = cms.Process('GEMCSCSegmentTest',Run3)

# import of standard configurations
process.load("FWCore.MessageService.MessageLogger_cfi")
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.EventContent.EventContent_cff')
process.load("Geometry.MuonNumbering.muonNumberingInitialization_cfi")
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase1_2021_realistic', '')

from FWCore.ParameterSet.VarParsing import VarParsing
options = VarParsing('analysis')
options.parseArguments()

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(options.maxEvents),
    output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
)

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(options.inputFiles),
)

process.gemcscs = cms.EDAnalyzer('TestGEMCSCSegmentAnalyzer',
    RootFileName = cms.untracked.string("TestGEMCSCSegmentHistograms.root"),
    Debug = cms.untracked.bool(True),
)

process.p = cms.Path(process.gemcscs)
