# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step2 --conditions auto:phase1_2022_realistic --datatier GEN-SIM-RECO --era Run3 --eventcontent RECOSIM --filein dbs:/RelValZMM_14/CMSSW_12_5_0_pre3-PU_124X_mcRun3_2022_realistic_v8-v1/GEN-SIM-DIGI-RAW --fileout file:step2.root --geometry DB:Extended --no_exec --number -1 --python_filename runRecoWithPSimHit.py --step RAW2DIGI,L1Reco,RECO
import FWCore.ParameterSet.Config as cms # type: ignore

from Configuration.Eras.Era_Run3_cff import Run3 # type: ignore

process = cms.Process('RECO',Run3)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.L1Reco_cff')
process.load('Configuration.StandardSequences.Reconstruction_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load('RecoLocalMuon.GEMCSCSegment.gemcscSegments_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1),
    output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(
    FailPath = cms.untracked.vstring(),
    IgnoreCompletely = cms.untracked.vstring(),
    Rethrow = cms.untracked.vstring(),
    SkipEvent = cms.untracked.vstring(),
    accelerators = cms.untracked.vstring('*'),
    allowUnscheduled = cms.obsolete.untracked.bool,
    canDeleteEarly = cms.untracked.vstring(),
    deleteNonConsumedUnscheduledModules = cms.untracked.bool(True),
    dumpOptions = cms.untracked.bool(False),
    emptyRunLumiMode = cms.obsolete.untracked.string,
    eventSetup = cms.untracked.PSet(
        forceNumberOfConcurrentIOVs = cms.untracked.PSet(
            allowAnyLabel_=cms.required.untracked.uint32
        ),
        numberOfConcurrentIOVs = cms.untracked.uint32(0)
    ),
    fileMode = cms.untracked.string('FULLMERGE'),
    forceEventSetupCacheClearOnNewRun = cms.untracked.bool(False),
    makeTriggerResults = cms.obsolete.untracked.bool,
    numberOfConcurrentLuminosityBlocks = cms.untracked.uint32(0),
    numberOfConcurrentRuns = cms.untracked.uint32(1),
    numberOfStreams = cms.untracked.uint32(0),
    numberOfThreads = cms.untracked.uint32(1),
    printDependencies = cms.untracked.bool(False),
    sizeOfStackForThreadsInKB = cms.optional.untracked.uint32,
    throwIfIllegalParameter = cms.untracked.bool(True),
    wantSummary = cms.untracked.bool(False)
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step2 nevts:-1'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.RECOSIMoutput = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM-RECO'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('file:step2.root'),
    outputCommands = process.RECOSIMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# RecoLocalMuon/GEMCSCSegment/test/runGEMCSCSegmentProducer_cfg.py
process.RECOSIMEventContent.outputCommands.extend([
    'keep  *_gemcscSegments_*_*',
    'keep  *_*csc*_*_*',
    'keep  *_*dt*_*_*',
    'keep  *_*gem*_*_*',
    'keep  *_*rpc*_*_*',
    'keep  *_*muon*_*_*',
    'keep  *_*CSC*_*_*',
    'keep  *_*DT*_*_*',
    'keep  *_*GEM*_*_*',
    'keep  *_*RPC*_*_*',
    'keep  *_*MUON*_*_*',
    'keep  *_*_*csc*_*',
    'keep  *_*_*dt*_*',
    'keep  *_*_*gem*_*',
    'keep  *_*_*rpc*_*',
    'keep  *_*_*muon*_*',
    'keep  *_*_*CSC*_*',
    'keep  *_*_*DT*_*',
    'keep  *_*_*GEM*_*',
    'keep  *_*_*RPC*_*',
    'keep  *_*_*MUON*_*',
    'keep  *SimTrack*_*_*_*',
])

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag # type: ignore
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase1_2022_realistic', '')

# Path and EndPath definitions
process.raw2digi_step = cms.Path(process.RawToDigi)
process.L1Reco_step = cms.Path(process.L1Reco)
process.reconstruction_step = cms.Path(process.reconstruction)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RECOSIMoutput_step = cms.EndPath(process.RECOSIMoutput)

process.gemcscSegments_step = cms.Path(process.gemcscSegments)

# Schedule definition
process.schedule = cms.Schedule(
    process.raw2digi_step,
    process.L1Reco_step,
    process.reconstruction_step,
    process.gemcscSegments_step,
    process.endjob_step,
    process.RECOSIMoutput_step
)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask # type: ignore
associatePatAlgosToolsTask(process)



# Customisation from command line

#Have logErrorHarvester wait for the same EDProducers to finish as those providing data for the OutputModule
from FWCore.Modules.logErrorHarvester_cff import customiseLogErrorHarvesterUsingOutputCommands # type: ignore
process = customiseLogErrorHarvesterUsingOutputCommands(process)

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete # type: ignore
process = customiseEarlyDelete(process)
# End adding early deletion

from FWCore.ParameterSet.VarParsing import VarParsing # type: ignore
options = VarParsing('analysis')
options.parseArguments()
process.maxEvents.input = options.maxEvents
process.source.fileNames = options.inputFiles
process.RECOSIMoutput.fileName = options.outputFile

process.options.accelerators = ["cpu"]

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.threshold = "DEBUG"
process.MessageLogger.debugModules = ["*"]
