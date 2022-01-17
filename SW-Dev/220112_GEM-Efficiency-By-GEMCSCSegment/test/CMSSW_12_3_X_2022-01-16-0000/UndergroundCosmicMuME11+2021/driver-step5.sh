CONDITIONS=auto:phase1_2021_cosmics
SCENARIO=cosmics
ERA=Run3
GEOMETRY=DB:Extended
MAG_FIELD=0T

COMMON_ARGS="--mc --conditions ${CONDITIONS} --era ${ERA} --scenario ${SCENARIO} --geometry ${GEOMETRY} --magField ${MAG_FIELD}"

cmsDriver.py step5 \
    ${COMMON_ARGS} \
    --step HARVESTING:gemClientsCosmics \
    --filetype DQM \
    --number -1  \
    --filein file:step4.root \
    --fileout file:step5.root \
    --no_exec
