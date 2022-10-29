# Path and EndPath definitions
process.gemEffByGEMCSCSegmentClientSeq = cms.Sequence(
    process.gemEffByGEMCSCSegmentClient +
    process.gemEffByGEMCSCSegmentClientNoChErr,
)


process.gemClients_step = cms.Path(process.gemClients)
process.gemEffByGEMCSCSegmentClient_step = cms.Path(process.gemEffByGEMCSCSegmentClientSeq)
process.dqmsave_step = cms.Path(process.DQMSaver)

# Schedule definition
process.schedule = cms.Schedule(
    process.gemClients_step,
    process.gemEffByGEMCSCSegmentClient_step,
    process.dqmsave_step
)
