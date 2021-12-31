#!/usr/bin/env sh
runTheMatrix.py -w upgrade -l 11650.0 > pp-2021-ZMM.txt 2>&1 &
runTheMatrix.py -w upgrade -l 35050.0 > pp-2026-ZMM.txt 2>&1 &

# In step2, the EventContent is FEVTDEBUGHLTEventContent but there is no
# there is no FEVTDEBUGHLTEventContent in Configuration/EventContent/python/EventContentCosmics_cff.py
runTheMatrix.py -w upgrade -l 11654.0 --command "--scenario cosmics" --apply "step2","--eventcontent FEVTDEBUG" > cosmics-2021-CosmicsSPLoose.txt 2>&1 &
runTheMatrix.py -w upgrade -l 35054.0 --command "--scenario cosmics" --apply "step2","--eventcontent FEVTDEBUG" > cosmics-2026-CosmicsSPLoose.txt 2>&1 &
