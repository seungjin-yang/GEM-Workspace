import FWCore.ParameterSet.Config as cms # type: ignore

from Configuration.Eras.Era_Run3_cff import Run3 # type: ignore

process = cms.Process("TestGEMCSCSegment", Run3)

process.load("FWCore.MessageService.MessageLogger_cfi")
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

from Configuration.AlCa.GlobalTag import GlobalTag # type: ignore
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase1_2022_realistic', '')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring()
)

process.gemcscs = cms.EDAnalyzer('TestGEMCSCSegmentAnalyzer',
    RootFileName = cms.untracked.string('file:output.root'),
    Debug = cms.untracked.bool(True),
)

process.p = cms.Path(process.gemcscs)

from FWCore.ParameterSet.VarParsing import VarParsing # type: ignore
options = VarParsing('analysis')
options.parseArguments()
process.maxEvents.input = options.maxEvents
process.source.fileNames = options.inputFiles
process.gemcscs.RootFileName = options.outputFile
