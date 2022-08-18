# GEM-Workspace
git config --local status.showUntrackedFiles no
https://cmsweb.cern.ch/dqm/relval/data/browse/ROOT/


## Snippents
###
```bash
git clone git@github.com:seungjin-yang/GEMDQMUtils.git
```

### for the cfg file with `EmptySource`
```python
process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.threshold = "DEBUG"
process.MessageLogger.debugModules = ["*"]

from IOMC.RandomEngine.RandomServiceHelper import RandomNumberServiceHelper
randSvc = RandomNumberServiceHelper(process.RandomNumberGeneratorService)
randSvc.populate()
```

### for the configuration file with `PoolSource`
```python
process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.threshold = "DEBUG"
process.MessageLogger.debugModules = ["*"]

from FWCore.ParameterSet.VarParsing import VarParsing
options = VarParsing('analysis')
options.parseArguments()
process.maxEvents.input = options.maxEvents
process.source.fileNames = options.inputFiles
```

### for step3 cfg
```python
process.RECOSIMoutput.outputCommands.extend([
    'keep *_*GEM*_*_*',
    'keep *_*gem*_*_*',
])
```
