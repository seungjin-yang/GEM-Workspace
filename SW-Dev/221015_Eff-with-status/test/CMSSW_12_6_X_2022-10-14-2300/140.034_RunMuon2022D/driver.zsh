cmsDriver.py step2  \
    --process reHLT \
    --step L1REPACK:Full,HLT:@relval2022 \
    --conditions auto:run3_hlt_relval \
    --data  \
    --eventcontent FEVTDEBUGHLT \
    --datatier FEVTDEBUGHLT \
    --era Run3 \
    --number -1  \
    --filein filelist:step1_dasquery.log \
    --lumiToProcess step1_lumiRanges.log \
    --fileout file:step2.root \
    --no_exec

cmsDriver.py step3  \
    --conditions auto:run3_data_relval \
    --step RAW2DIGI,L1Reco,RECO \
    --datatier RECO \
    --eventcontent RECO \
    --data  \
    --process reRECO \
    --scenario pp \
    --era Run3 \
    --customise Configuration/DataProcessing/RecoTLR.customisePostEra_Run3 \
    --number -1  \
    --filein  file:step2.root  \
    --fileout file:step3.root  \
    --no_exec

cmsDriver.py step4  \
    --conditions auto:run3_data_relval \
    --step DQM:gemSources \
    --datatier DQMIO \
    --eventcontent DQM \
    --data  \
    --process reRECO \
    --scenario pp \
    --era Run3 \
    --customise Configuration/DataProcessing/RecoTLR.customisePostEra_Run3 \
    --number -1  \
    --filein  file:step3.root  \
    --fileout file:step4.root  \
    --no_exec

cmsDriver.py step5  \
    --step HARVESTING:gemClients \
    --conditions auto:run3_data \
    --data  \
    --filetype DQM \
    --scenario pp \
    --number -1  \
    --filein file:step4.root \
    --fileout file:step5.root  \
    --no_exec
