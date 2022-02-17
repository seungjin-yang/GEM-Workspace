# GEM-Workspace
git config --local status.showUntrackedFiles no
https://cmsweb.cern.ch/dqm/relval/data/browse/ROOT/


## Snippents
### for the cfg file with `EmptySource`
```python
from IOMC.RandomEngine.RandomServiceHelper import RandomNumberServiceHelper
randSvc = RandomNumberServiceHelper(process.RandomNumberGeneratorService)
randSvc.populate()
```

### for the configuration file with `PoolSource`
```python
from FWCore.ParameterSet.VarParsing import VarParsing
options = VarParsing('analysis')
options.parseArguments()

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(options.inputFiles),
)
```

### for step3 cfg
```python
process.RECOSIMoutput.outputCommands.extend([
    'keep *_*GEM*_*_*',
    'keep *_*gem*_*_*',
])
```
