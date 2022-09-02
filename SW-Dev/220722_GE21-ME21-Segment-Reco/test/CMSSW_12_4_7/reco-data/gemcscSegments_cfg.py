# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: gemcscSegments --conditions 124X_dataRun3_Express_v5 --era Run3 --eventcontent RAWRECO --filein file:input.root --fileout file:output.root --geometry DB:Extended --no_exec --number -1 --step RECO --python_filename gemcscSegments_cfg.py
import FWCore.ParameterSet.Config as cms # type: ignore

from Configuration.Eras.Era_Run3_cff import Run3 # type: ignore

process_name = 'GEMCSCSegmentRECO'
process = cms.Process(process_name, Run3)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
# process.load('Configuration.StandardSequences.Reconstruction_Data_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.load('RecoLocalMuon.GEMRecHit.gemRecHits_cfi')
process.load('RecoLocalMuon.GEMCSCSegment.gemcscSegments_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1),
    output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('file:input.root'),
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
    annotation = cms.untracked.string('gemcscSegments nevts:-1'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.RAWRECOoutput = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string(''),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('file:output.root'),
    outputCommands = process.RAWRECOEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)
process.RAWRECOoutput.outputCommands.extend([
    'keep  *_gemRecHits_*_*' ,
    'keep  *_gemcscSegments_*_*' ,
])


# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag # type: ignore
process.GlobalTag = GlobalTag(process.GlobalTag, '124X_dataRun3_Express_v5', '')
process.GlobalTag.connect = 'frontier://PromptProd/CMS_CONDITIONS'

# Path and EndPath definitions
process.gemRecHits = process.gemRecHits.clone(ge21Off=False)
process.gemcscSegments.inputObjectsGEM = cms.InputTag("gemRecHits", "", process_name)

process.gemSeq = cms.Sequence(
    process.gemRecHits *
    process.gemcscSegments,
)

process.gemSeq_step = cms.Path(process.gemSeq)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RAWRECOoutput_step = cms.EndPath(process.RAWRECOoutput)

# Schedule definition
process.schedule = cms.Schedule(
    process.gemSeq_step,
    process.endjob_step,
    process.RAWRECOoutput_step
)

# Customisation from command line

#Have logErrorHarvester wait for the same EDProducers to finish as those providing data for the OutputModule
from FWCore.Modules.logErrorHarvester_cff import customiseLogErrorHarvesterUsingOutputCommands
process = customiseLogErrorHarvesterUsingOutputCommands(process)

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion



from FWCore.ParameterSet.VarParsing import VarParsing # type: ignore
options = VarParsing('analysis')
options.parseArguments()
process.maxEvents.input = options.maxEvents
process.source.fileNames = options.inputFiles
process.RAWRECOoutput.fileName = options.outputFile
