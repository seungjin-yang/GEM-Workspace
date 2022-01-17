CONDITIONS=auto:phase1_2021_cosmics
SCENARIO=cosmics
ERA=Run3
GEOMETRY=DB:Extended
MAG_FIELD=0T

COMMON_ARGS="--mc --conditions ${CONDITIONS} --era ${ERA} --scenario ${SCENARIO} --geometry ${GEOMETRY} --magField ${MAG_FIELD}"

cmsDriver.py step4 \
    ${COMMON_ARGS} \
	--step DQM \
	--datatier DQMIO \
	--number -1 \
	--eventcontent DQM \
	--filein file:step3.root \
	--fileout file:step4.root \
    --no_exec
