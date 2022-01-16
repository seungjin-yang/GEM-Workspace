# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step5 -s ALCA:SiPixelCalSingleMuonLoose+SiPixelCalSingleMuonTight+TkAlMuonIsolated+TkAlMinBias+MuAlOverlaps+EcalESAlign+TkAlZMuMu+TkAlDiMuonAndVertex+HcalCalHBHEMuonFilter+TkAlUpsilonMuMu+TkAlJpsiMuMu+SiStripCalMinBias --conditions auto:phase1_2021_realistic --datatier ALCARECO -n 10 --eventcontent ALCARECO --geometry DB:Extended --filein file:step3.root --era Run3 --fileout file:step5.root
import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Run3_cff import Run3

process = cms.Process('ALCA',Run3)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.AlCaRecoStreams_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10),
    output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('file:step3.root'),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(
    FailPath = cms.untracked.vstring(),
    IgnoreCompletely = cms.untracked.vstring(),
    Rethrow = cms.untracked.vstring(),
    SkipEvent = cms.untracked.vstring(),
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
    annotation = cms.untracked.string('step5 nevts:10'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition


# Additional output definition
process.ALCARECOStreamEcalESAlign = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOEcalESAlign')
    ),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('ALCARECO'),
        filterName = cms.untracked.string('EcalESAlign')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    fileName = cms.untracked.string('EcalESAlign.root'),
    outputCommands = cms.untracked.vstring(
        'drop *',
        'keep ESDigiCollection_ecalPreshowerDigis_*_*',
        'keep SiPixelClusteredmNewDetSetVector_ecalAlCaESAlignTrackReducer_*_*',
        'keep SiStripClusteredmNewDetSetVector_ecalAlCaESAlignTrackReducer_*_*',
        'keep TrackingRecHitsOwned_ecalAlCaESAlignTrackReducer_*_*',
        'keep recoTrackExtras_ecalAlCaESAlignTrackReducer_*_*',
        'keep recoTracks_ecalAlCaESAlignTrackReducer_*_*',
        'keep recoBeamSpot_offlineBeamSpot_*_*'
    )
)
process.ALCARECOStreamHcalCalHBHEMuonFilter = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOHcalCalHBHEMuonFilter')
    ),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('ALCARECO'),
        filterName = cms.untracked.string('HcalCalHBHEMuonFilter')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    fileName = cms.untracked.string('HcalCalHBHEMuonFilter.root'),
    outputCommands = cms.untracked.vstring(
        'drop *',
        'keep *_hbhereco_*_*',
        'keep *_ecalRecHit_*_*',
        'keep *_offlineBeamSpot_*_*',
        'keep *_TriggerResults_*_*',
        'keep HcalNoiseSummary_hcalnoise_*_*',
        'keep recoTracks_globalMuons_*_*',
        'keep recoTrackExtras_globalMuons_*_*',
        'keep recoTracks_standAloneMuons_*_*',
        'keep recoTrackExtras_standAloneMuons_*_*',
        'keep recoTracks_generalTracks_*_*',
        'keep recoTrackExtras_generalTracks_*_*',
        'keep recoTracks_tevMuons_*_*',
        'keep recoTrackExtras_tevMuons_*_*',
        'keep *_offlinePrimaryVertices_*_*',
        'keep *_scalersRawToDigi_*_*',
        'keep *_muons_*_*'
    )
)
process.ALCARECOStreamMuAlOverlaps = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOMuAlOverlaps')
    ),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('ALCARECO'),
        filterName = cms.untracked.string('MuAlOverlaps')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    fileName = cms.untracked.string('MuAlOverlaps.root'),
    outputCommands = cms.untracked.vstring(
        'drop *',
        'keep *_ALCARECOMuAlOverlaps_*_*',
        'keep *_ALCARECOMuAlOverlapsGeneralTracks_*_*',
        'keep *_muonCSCDigis_*_*',
        'keep *_muonDTDigis_*_*',
        'keep *_muonRPCDigis_*_*',
        'keep *_dt1DRecHits_*_*',
        'keep *_dt2DSegments_*_*',
        'keep *_dt4DSegments_*_*',
        'keep *_csc2DRecHits_*_*',
        'keep *_cscSegments_*_*',
        'keep *_rpcRecHits_*_*',
        'keep L1AcceptBunchCrossings_*_*_*',
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*',
        'keep *_TriggerResults_*_*',
        'keep *_offlineBeamSpot_*_*',
        'keep *_offlinePrimaryVertices_*_*',
        'keep DcsStatuss_scalersRawToDigi_*_*'
    )
)
process.ALCARECOStreamSiPixelCalSingleMuonLoose = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOSiPixelCalSingleMuonLoose')
    ),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('ALCARECO'),
        filterName = cms.untracked.string('SiPixelCalSingleMuonLoose')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    fileName = cms.untracked.string('SiPixelCalSingleMuonLoose.root'),
    outputCommands = cms.untracked.vstring(
        'drop *',
        'keep *_ALCARECOSiPixelCalSingleMuonLoose_*_*',
        'keep *_muons__*',
        'keep *_offlinePrimaryVertices_*_*',
        'keep *_*riggerResults_*_HLT'
    )
)
process.ALCARECOStreamSiPixelCalSingleMuonTight = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOSiPixelCalSingleMuonTight')
    ),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('ALCARECO'),
        filterName = cms.untracked.string('SiPixelCalSingleMuonTight')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    fileName = cms.untracked.string('SiPixelCalSingleMuonTight.root'),
    outputCommands = cms.untracked.vstring(
        'drop *',
        'keep *_ALCARECOSiPixelCalSingleMuonTight_*_*',
        'keep *_muons__*',
        'keep *_offlinePrimaryVertices_*_*',
        'keep *_*riggerResults_*_HLT',
        'keep *_*closebyPixelClusters*_*_*',
        'keep *_*trackDistances*_*_*'
    )
)
process.ALCARECOStreamSiStripCalMinBias = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOSiStripCalMinBias')
    ),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('ALCARECO'),
        filterName = cms.untracked.string('SiStripCalMinBias')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    fileName = cms.untracked.string('SiStripCalMinBias.root'),
    outputCommands = cms.untracked.vstring(
        'drop *',
        'keep *_ALCARECOSiStripCalMinBias_*_*',
        'keep *_siStripClusters_*_*',
        'keep *_siPixelClusters_*_*',
        'keep DetIdedmEDCollection_siStripDigis_*_*',
        'keep L1AcceptBunchCrossings_*_*_*',
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*',
        'keep LumiScalerss_scalersRawToDigi_*_*',
        'keep DcsStatuss_scalersRawToDigi_*_*',
        'keep *_TriggerResults_*_*'
    )
)
process.ALCARECOStreamTkAlDiMuonAndVertex = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOTkAlDiMuonAndVertex')
    ),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('ALCARECO'),
        filterName = cms.untracked.string('TkAlDiMuonAndVertex')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    fileName = cms.untracked.string('TkAlDiMuonAndVertex.root'),
    outputCommands = cms.untracked.vstring(
        'drop *',
        'keep *_ALCARECOTkAlDiMuon_*_*',
        'keep *_ALCARECOTkAlDiMuonVertexTracks_*_*',
        'keep L1AcceptBunchCrossings_*_*_*',
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*',
        'keep *_TriggerResults_*_*',
        'keep DcsStatuss_scalersRawToDigi_*_*',
        'keep *_offlinePrimaryVertices_*_*'
    )
)
process.ALCARECOStreamTkAlJpsiMuMu = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOTkAlJpsiMuMu')
    ),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('ALCARECO'),
        filterName = cms.untracked.string('TkAlJpsiMuMu')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    fileName = cms.untracked.string('TkAlJpsiMuMu.root'),
    outputCommands = cms.untracked.vstring(
        'drop *',
        'keep *_ALCARECOTkAlJpsiMuMu_*_*',
        'keep L1AcceptBunchCrossings_*_*_*',
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*',
        'keep *_TriggerResults_*_*',
        'keep DcsStatuss_scalersRawToDigi_*_*',
        'keep *_offlinePrimaryVertices_*_*'
    )
)
process.ALCARECOStreamTkAlMinBias = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOTkAlMinBias')
    ),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('ALCARECO'),
        filterName = cms.untracked.string('TkAlMinBias')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    fileName = cms.untracked.string('TkAlMinBias.root'),
    outputCommands = cms.untracked.vstring(
        'drop *',
        'keep *_ALCARECOTkAlMinBias_*_*',
        'keep L1AcceptBunchCrossings_*_*_*',
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*',
        'keep *_TriggerResults_*_*',
        'keep DcsStatuss_scalersRawToDigi_*_*',
        'keep *_offlinePrimaryVertices_*_*',
        'keep *_offlineBeamSpot_*_*'
    )
)
process.ALCARECOStreamTkAlMuonIsolated = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOTkAlMuonIsolated')
    ),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('ALCARECO'),
        filterName = cms.untracked.string('TkAlMuonIsolated')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    fileName = cms.untracked.string('TkAlMuonIsolated.root'),
    outputCommands = cms.untracked.vstring(
        'drop *',
        'keep *_ALCARECOTkAlMuonIsolated_*_*',
        'keep L1AcceptBunchCrossings_*_*_*',
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*',
        'keep *_TriggerResults_*_*',
        'keep DcsStatuss_scalersRawToDigi_*_*',
        'keep *_offlinePrimaryVertices_*_*'
    )
)
process.ALCARECOStreamTkAlUpsilonMuMu = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOTkAlUpsilonMuMu')
    ),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('ALCARECO'),
        filterName = cms.untracked.string('TkAlUpsilonMuMu')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    fileName = cms.untracked.string('TkAlUpsilonMuMu.root'),
    outputCommands = cms.untracked.vstring(
        'drop *',
        'keep *_ALCARECOTkAlUpsilonMuMu_*_*',
        'keep L1AcceptBunchCrossings_*_*_*',
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*',
        'keep *_TriggerResults_*_*',
        'keep DcsStatuss_scalersRawToDigi_*_*',
        'keep *_offlinePrimaryVertices_*_*'
    )
)
process.ALCARECOStreamTkAlZMuMu = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOTkAlZMuMu')
    ),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('ALCARECO'),
        filterName = cms.untracked.string('TkAlZMuMu')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    fileName = cms.untracked.string('TkAlZMuMu.root'),
    outputCommands = cms.untracked.vstring(
        'drop *',
        'keep *_ALCARECOTkAlZMuMu_*_*',
        'keep L1AcceptBunchCrossings_*_*_*',
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*',
        'keep *_TriggerResults_*_*',
        'keep DcsStatuss_scalersRawToDigi_*_*',
        'keep *_offlinePrimaryVertices_*_*'
    )
)

# Other statements
process.ALCARECOEventContent.outputCommands.extend(process.OutALCARECOTkAlMinBias_noDrop.outputCommands)
process.ALCARECOEventContent.outputCommands.extend(process.OutALCARECOTkAlMuonIsolated_noDrop.outputCommands)
process.ALCARECOEventContent.outputCommands.extend(process.OutALCARECOTkAlZMuMu_noDrop.outputCommands)
process.ALCARECOEventContent.outputCommands.extend(process.OutALCARECOTkAlDiMuonAndVertex_noDrop.outputCommands)
process.ALCARECOEventContent.outputCommands.extend(process.OutALCARECOTkAlJpsiMuMu_noDrop.outputCommands)
process.ALCARECOEventContent.outputCommands.extend(process.OutALCARECOTkAlUpsilonMuMu_noDrop.outputCommands)
process.ALCARECOEventContent.outputCommands.extend(process.OutALCARECOSiPixelCalSingleMuonLoose_noDrop.outputCommands)
process.ALCARECOEventContent.outputCommands.extend(process.OutALCARECOSiPixelCalSingleMuonTight_noDrop.outputCommands)
process.ALCARECOEventContent.outputCommands.extend(process.OutALCARECOSiStripCalMinBias_noDrop.outputCommands)
process.ALCARECOEventContent.outputCommands.extend(process.OutALCARECOEcalESAlign_noDrop.outputCommands)
process.ALCARECOEventContent.outputCommands.extend(process.OutALCARECOHcalCalHBHEMuonFilter_noDrop.outputCommands)
process.ALCARECOEventContent.outputCommands.extend(process.OutALCARECOMuAlOverlaps_noDrop.outputCommands)
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase1_2021_realistic', '')

# Path and EndPath definitions
process.endjob_step = cms.EndPath(process.endOfProcess)
process.ALCARECOStreamEcalESAlignOutPath = cms.EndPath(process.ALCARECOStreamEcalESAlign)
process.ALCARECOStreamHcalCalHBHEMuonFilterOutPath = cms.EndPath(process.ALCARECOStreamHcalCalHBHEMuonFilter)
process.ALCARECOStreamMuAlOverlapsOutPath = cms.EndPath(process.ALCARECOStreamMuAlOverlaps)
process.ALCARECOStreamSiPixelCalSingleMuonLooseOutPath = cms.EndPath(process.ALCARECOStreamSiPixelCalSingleMuonLoose)
process.ALCARECOStreamSiPixelCalSingleMuonTightOutPath = cms.EndPath(process.ALCARECOStreamSiPixelCalSingleMuonTight)
process.ALCARECOStreamSiStripCalMinBiasOutPath = cms.EndPath(process.ALCARECOStreamSiStripCalMinBias)
process.ALCARECOStreamTkAlDiMuonAndVertexOutPath = cms.EndPath(process.ALCARECOStreamTkAlDiMuonAndVertex)
process.ALCARECOStreamTkAlJpsiMuMuOutPath = cms.EndPath(process.ALCARECOStreamTkAlJpsiMuMu)
process.ALCARECOStreamTkAlMinBiasOutPath = cms.EndPath(process.ALCARECOStreamTkAlMinBias)
process.ALCARECOStreamTkAlMuonIsolatedOutPath = cms.EndPath(process.ALCARECOStreamTkAlMuonIsolated)
process.ALCARECOStreamTkAlUpsilonMuMuOutPath = cms.EndPath(process.ALCARECOStreamTkAlUpsilonMuMu)
process.ALCARECOStreamTkAlZMuMuOutPath = cms.EndPath(process.ALCARECOStreamTkAlZMuMu)

# Schedule definition
process.schedule = cms.Schedule(process.pathALCARECOTkAlMinBias,process.pathALCARECOTkAlMuonIsolated,process.pathALCARECOTkAlZMuMu,process.pathALCARECOTkAlDiMuonAndVertex,process.pathALCARECOTkAlJpsiMuMu,process.pathALCARECOTkAlUpsilonMuMu,process.pathALCARECOSiPixelCalSingleMuonLoose,process.pathALCARECOSiPixelCalSingleMuonTight,process.pathALCARECOSiStripCalMinBias,process.pathALCARECOEcalESAlign,process.pathALCARECOHcalCalHBHEMuonFilter,process.pathALCARECOMuAlOverlaps,process.pathALCARECOMuAlOverlapsGeneralTracks,process.endjob_step,process.ALCARECOStreamEcalESAlignOutPath,process.ALCARECOStreamHcalCalHBHEMuonFilterOutPath,process.ALCARECOStreamMuAlOverlapsOutPath,process.ALCARECOStreamSiPixelCalSingleMuonLooseOutPath,process.ALCARECOStreamSiPixelCalSingleMuonTightOutPath,process.ALCARECOStreamSiStripCalMinBiasOutPath,process.ALCARECOStreamTkAlDiMuonAndVertexOutPath,process.ALCARECOStreamTkAlJpsiMuMuOutPath,process.ALCARECOStreamTkAlMinBiasOutPath,process.ALCARECOStreamTkAlMuonIsolatedOutPath,process.ALCARECOStreamTkAlUpsilonMuMuOutPath,process.ALCARECOStreamTkAlZMuMuOutPath)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)



# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
