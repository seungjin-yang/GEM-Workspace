from WMCore.Configuration import Configuration

config = Configuration()
config.section_('General')
config.General.transferOutputs = True

config.section_('JobType')
config.JobType.pluginName = 'Analysis'

config.section_('Data')
config.Data.publication = False

# config.Data.splitting = 'Automatic'

config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1


config.section_('Site')
config.Site.storageSite = 'T3_KR_UOS'
