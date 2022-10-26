# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step2 --process reHLT --step L1REPACK:Full,HLT:@relval2022 --conditions auto:run3_hlt_relval --data --eventcontent FEVTDEBUGHLT --datatier FEVTDEBUGHLT --era Run3 --number -1 --filein filelist:step1_dasquery.log --lumiToProcess step1_lumiRanges.log --fileout file:step2.root --no_exec
import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Run3_cff import Run3

process = cms.Process('reHLT',Run3)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.SimL1EmulatorRepack_Full_cff')
process.load('HLTrigger.Configuration.HLT_GRun_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1),
    output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        '/store/data/Run2022D/Muon/RAW/v1/000/357/538/00000/07ecabd8-37cb-4554-abed-c67247854b40.root',
        '/store/data/Run2022D/Muon/RAW/v1/000/357/538/00000/1e360ddd-aec3-4cb2-9b27-ed6691059377.root',
        '/store/data/Run2022D/Muon/RAW/v1/000/357/538/00000/3db9c845-a616-4ea4-a57e-58dbd7b79f9f.root',
        '/store/data/Run2022D/Muon/RAW/v1/000/357/538/00000/55a4763b-de96-4883-993d-f8b0d91f31ec.root',
        '/store/data/Run2022D/Muon/RAW/v1/000/357/538/00000/5e5a5ee0-6035-4f56-b156-d1592b552ab1.root',
        '/store/data/Run2022D/Muon/RAW/v1/000/357/538/00000/6e2e415f-7787-48d2-abef-8a8a9c82fdeb.root',
        '/store/data/Run2022D/Muon/RAW/v1/000/357/538/00000/709a03e4-531a-48ba-b31d-a56daf75ad61.root',
        '/store/data/Run2022D/Muon/RAW/v1/000/357/538/00000/78a9c700-a249-4831-95aa-cf43c67ab824.root',
        '/store/data/Run2022D/Muon/RAW/v1/000/357/538/00000/80c76f1c-55f6-4375-b9d0-7c2c0dfcf814.root',
        '/store/data/Run2022D/Muon/RAW/v1/000/357/538/00000/8a94da59-7012-4e3e-a08f-09b28b0c1985.root',
        '/store/data/Run2022D/Muon/RAW/v1/000/357/538/00000/93f5a8a8-19d4-4557-ae10-62f505a0aff7.root',
        '/store/data/Run2022D/Muon/RAW/v1/000/357/538/00000/949db0b8-e123-4cca-8a94-155fcfb72adb.root',
        '/store/data/Run2022D/Muon/RAW/v1/000/357/538/00000/b9bc4b83-86cf-4a73-8c23-27a20fbef398.root',
        '/store/data/Run2022D/Muon/RAW/v1/000/357/538/00000/c1c25265-810f-4143-bbaf-a0c94c850848.root',
        '/store/data/Run2022D/Muon/RAW/v1/000/357/538/00000/c51c3eb0-fca5-4959-8c52-414d912de7de.root',
        '/store/data/Run2022D/Muon/RAW/v1/000/357/538/00000/d6ddf278-35dd-4ad7-8bef-ea40b97d19a7.root',
        '/store/data/Run2022D/Muon/RAW/v1/000/357/538/00000/de537464-89e4-4636-88c1-6f7850d3d852.root',
        '/store/data/Run2022D/Muon/RAW/v1/000/357/538/00000/deee0bb6-ffb4-4376-ba5c-777e7ff340f2.root',
        '/store/data/Run2022D/Muon/RAW/v1/000/357/538/00000/e0b991ef-6cc5-4e74-9407-124e4894797c.root',
        '/store/data/Run2022D/Muon/RAW/v1/000/357/538/00000/e787cf74-273a-4e4f-9012-cc860559fa4c.root',
        '/store/data/Run2022D/Muon/RAW/v1/000/357/538/00000/f15d5ff4-b67f-4c85-b952-c25ad8f0468d.root',
        '/store/data/Run2022D/Muon/RAW/v1/000/357/538/00000/f8d02415-8872-4a68-b17d-b0a6bfe9d3f0.root',
        '/store/data/Run2022D/Muon/RAW/v1/000/357/538/00000/fd94730f-edda-474c-b89f-cd815dacde9a.root'
    ),
    lumisToProcess = cms.untracked.VLuminosityBlockRange("357538:39-357538:63"),
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
    holdsReferencesToDeleteEarly = cms.untracked.VPSet(),
    makeTriggerResults = cms.obsolete.untracked.bool,
    modulesToIgnoreForDeleteEarly = cms.untracked.vstring(),
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

process.FEVTDEBUGHLToutput = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('FEVTDEBUGHLT'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('file:step2.root'),
    outputCommands = process.FEVTDEBUGHLTEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
from HLTrigger.Configuration.CustomConfigs import ProcessName
process = ProcessName(process)

from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run3_hlt_relval', '')

# Path and EndPath definitions
process.L1RePack_step = cms.Path(process.SimL1Emulator)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.FEVTDEBUGHLToutput_step = cms.EndPath(process.FEVTDEBUGHLToutput)

# Schedule definition
# process.schedule imported from cff in HLTrigger.Configuration
process.schedule.insert(0, process.L1RePack_step)
process.schedule.extend([process.endjob_step,process.FEVTDEBUGHLToutput_step])
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)



# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion

from FWCore.ParameterSet.VarParsing import VarParsing
options = VarParsing('analysis')
options.parseArguments()
process.maxEvents.input = options.maxEvents
process.source.fileNames = options.inputFiles

process.FEVTDEBUGHLToutput.outputCommands.extend([
    'keep *_muonGEMDigis_*_*',
    ])
