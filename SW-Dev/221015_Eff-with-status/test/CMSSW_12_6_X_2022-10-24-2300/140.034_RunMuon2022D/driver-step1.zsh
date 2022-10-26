# in: /eos/home-s/seyang/workspace/GEM/SW-Dev/221015_Eff-with-status/test/CMSSW_12_6_X_2022-10-24-2300 dryRun for 'cd 140.034_RunMuon2022D+RunMuon2022D+HLTRUN3+RECONANORUN3+HARVESTRUN3
 echo '{
"357538" : [[39, 63]]
}' > step1_lumiRanges.log  2>&1
 

# in: /eos/home-s/seyang/workspace/GEM/SW-Dev/221015_Eff-with-status/test/CMSSW_12_6_X_2022-10-24-2300 dryRun for 'cd 140.034_RunMuon2022D+RunMuon2022D+HLTRUN3+RECONANORUN3+HARVESTRUN3
 (dasgoclient --limit 0 --query 'lumi,file dataset=/Muon/Run2022D-v1/RAW run=357538' --format json | das-selected-lumis.py 39,63 ) | sort -u > step1_dasquery.log  2>&1
