# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.9.12 (main, Jun  1 2022, 11:38:51) 
# [GCC 7.5.0]
# Embedded file name: GEMDCSP5Monitor.py
# Compiled at: 2022-08-18 17:46:47
import cx_Oracle, ROOT, os, time
from datetime import datetime
from datetime import timedelta
from operator import itemgetter
from array import array
import argparse
from argparse import RawTextHelpFormatter
from sys import exit
descrString = 'Twiki\n------------------------\nTO BE DONE'
descrString = descrString + '\n\nEnvironment\n------------------------\nThis code runs on the 904DAQ machine\n'
descrString = descrString + '\nFirst of all you have to enter in your lxplus area and then connect to the 904DAQ machine'
descrString = descrString + '\nNow you have to ensure that in your area you have set two variables for access'
descrString = descrString + '\nGEM_P5_DB_NAME_OFFLINE_MONITOR and GEM_P5_DB_ACCOUNT_OFFLINE_MONITOR which contain the credentials to access to CMS P5 database'
descrString = descrString + '\n\nDescription\n------------------------\nRetrieve from the database the vmon, imon, status, isON and temperature informations\n'
descrString = descrString + 'To run this code you first have to put in one file the alias of chambers you want'
descrString = descrString + '\n   In case you want data for the present situation in P5'
descrString = descrString + '\n      HV data --> file to modifiy: P5GEMChosenChambers_HV.txt'
descrString = descrString + '\n      LV data --> file to modifiy: P5GEMChosenChambers_LV.txt'
descrString = descrString + '\n   In case you want data for the slice test period'
descrString = descrString + '\n      HV data --> file to modifiy: P5GEMChosenChambers_sliceTest_HV.txt'
descrString = descrString + '\n      LV data --> file to modifiy: P5GEMChosenChambers_sliceTest_LV.txt'
descrString = descrString + '\n\nExample\n------------------------'
descrString = descrString + '\npython GEMDCSP5Monitor.py sta_period end_period monitorFlag sliceTestFlag'
descrString = descrString + '\npython GEMDCSP5Monitor.py 2018-04-01_15:22:31 2018-04-02_15:22:31 HV 1'
parser = argparse.ArgumentParser(description=descrString, formatter_class=RawTextHelpFormatter)
parser.add_argument('sta_period', type=str, help='UTC Start Date of the monitor, has to be inserted in format YYYY-MM-DD HH24:mm:ss (e.g. 2018-04-01_15:22:31)', metavar='sta_period')
parser.add_argument('end_period', type=str, help='UTC End Date of the monitor, has to be inserted in format YYYY-MM-DD HH24:mm:ss (e.g. 2018-04-02_15:22:31)', metavar='end_period')
parser.add_argument('monitorFlag', type=str, help="monitorFlag tell if data must be read for HV or LV (monitorFlag accepts only 'HV' or 'LV' string)", metavar='monitorFlag')
parser.add_argument('sliceTestFlag', type=int, help='sliceTestFlag tells if data must be taken from slice test period or not \n(sliceTestFlag = 0 : I use data for current situation in P5, sliceTestFlag = 1 : I use data collected during the slice test)', metavar='sliceTestFlag')
parser.add_argument('--chamberList', '-c', type=str, help="custom list of Chosen Chambers. If not set, default files will be used. If set to 'all', all existing chambers will be used.)", metavar='chamberList')
parser.add_argument('--verbose', '--v', help='Enables print outputs.')
parser.add_argument('--save', '--s', help='Save .png plots.')
args = parser.parse_args()
ROOT.gROOT.SetBatch(True)
if args.verbose:

    def verboseprint(*args):
        for arg in args:
            print(arg, end=' ')

        print()


else:
    verboseprint = lambda *a: None
dbName = 'cms_omds_adg'
dbAccount = 'CMS_COND_GENERAL_R/p3105rof@'

def main():
    monitorFlag = args.monitorFlag
    sliceTestFlag = args.sliceTestFlag
    dir_path = os.path.dirname(os.path.realpath(__file__))
    if args.chamberList is not None and args.chamberList != 'all':
        chambersFileName == args.chamberList
    else:
        if args.chamberList == 'all':
            if sliceTestFlag == 0:
                chambersFileName = 'P5GEMExistingChambers.txt'
            if sliceTestFlag == 1:
                if monitorFlag == 'HV':
                    chambersFileName = 'P5GEMExistingChambers_sliceTest_HV.txt'
                if monitorFlag == 'LV':
                    chambersFileName = 'P5GEMExistingChambers_sliceTest_LV.txt'
        else:
            if monitorFlag == 'HV':
                if sliceTestFlag == 0:
                    chambersFileName = 'P5GEMChosenChambers_HV.txt'
                if sliceTestFlag == 1:
                    chambersFileName = 'P5GEMChosenChambers_sliceTest_HV.txt'
            else:
                if monitorFlag == 'LV':
                    if sliceTestFlag == 0:
                        chambersFileName = 'P5GEMChosenChambers_LV.txt'
                    if sliceTestFlag == 1:
                        chambersFileName = 'P5GEMChosenChambers_sliceTest_LV.txt'
                chambersFileName = dir_path + '/' + chambersFileName
                if sliceTestFlag == 0:
                    existingChambersFileName = 'P5GEMExistingChambers.txt'
                if sliceTestFlag == 1:
                    if monitorFlag == 'HV':
                        existingChambersFileName = 'P5GEMExistingChambers_sliceTest_HV.txt'
                    if monitorFlag == 'LV':
                        existingChambersFileName = 'P5GEMExistingChambers_sliceTest_LV.txt'
                existingChambersFileName = dir_path + '/' + existingChambersFileName
                if monitorFlag == 'HV':
                    if sliceTestFlag == 0:
                        mappingFileName = 'GEMP5MappingHV.txt'
                    if sliceTestFlag == 1:
                        mappingFileName = 'GEMP5MappingHV_sliceTest.txt'
                if monitorFlag == 'LV':
                    if sliceTestFlag == 0:
                        mappingFileName = 'GEMP5MappingLV.txt'
                    if sliceTestFlag == 1:
                        mappingFileName = 'GEMP5MappingLV_sliceTest.txt'
                mappingFileName = dir_path + '/' + mappingFileName
                sta_period = args.sta_period
                end_period = args.end_period
                sta_period.replace('_', ' ')
                end_period.replace('_', ' ')
                start = sta_period.replace(' ', '_')
                end = end_period.replace(' ', '_')
                start = start.replace(':', '-')
                end = end.replace(':', '-')
                sta_period = "'" + sta_period + "'"
                end_period = "'" + end_period + "'"
                startDate = datetime(int(start[:4]), int(start[5:7]), int(start[8:10]), int(start[11:13]), int(start[14:16]), int(start[17:]))
                endDate = datetime(int(end[:4]), int(end[5:7]), int(end[8:10]), int(end[11:13]), int(end[14:16]), int(end[17:]))
                if not os.path.exists(dir_path + '/OutputFiles'):
                    os.makedirs(dir_path + '/OutputFiles')
                dirStringSave = dir_path + '/OutputFiles/P5_GEM_' + monitorFlag + '_monitor_UTC_start_' + start + '_end_' + end + '/'
                fileName = dir_path + '/OutputFiles/P5_GEM_' + monitorFlag + '_monitor_UTC_start_' + start + '_end_' + end + '.root'
                f1 = ROOT.TFile(fileName, 'RECREATE')
                mappingChangeDate = []
                if sliceTestFlag == 1:
                    if monitorFlag == 'HV':
                        firstMappingChange = datetime(2017, 3, 18, 11, 54, 1)
                        secondMappingChange = datetime(2018, 3, 5, 4, 7, 16)
                        mappingChangeDate.append(firstMappingChange)
                        mappingChangeDate.append(secondMappingChange)
                    if monitorFlag == 'LV':
                        firstMappingChange = datetime(2017, 2, 15, 0, 0, 1)
                        secondMappingChange = datetime(2017, 6, 9, 16, 17, 4)
                        mappingChangeDate.append(firstMappingChange)
                        mappingChangeDate.append(secondMappingChange)
                if sliceTestFlag == 0:
                    if monitorFlag == 'HV':
                        firstMappingChange = datetime(2019, 10, 1, 0, 0, 1)
                        mappingChangeDate.append(firstMappingChange)
                    if monitorFlag == 'LV':
                        firstMappingChange = datetime(2019, 10, 1, 0, 0, 1)
                        mappingChangeDate.append(firstMappingChange)
                lastDate = datetime(2050, 1, 1, 0, 0, 1)
                mappingChangeDate.append(lastDate)
                periodBool = []
                numberOfMaps = len(mappingChangeDate) - 1
                for mapIdx in range(numberOfMaps):
                    periodBool.append(0)

                startIdx = -1
                endIdx = -1
                if startDate < mappingChangeDate[0] or endDate < mappingChangeDate[0]:
                    LowDateError = 'ERROR: Date too early!! Dates must be greater than ' + str(mappingChangeDate[0])
                    exit(LowDateError)
                if startDate > endDate:
                    SwapDateError = 'ERROR: Start date greater than end date!!'
                    exit(SwapDateError)
                startIdx = -1
                endIdx = -1
                for dateIdx in range(len(mappingChangeDate) - 1):
                    if startDate > mappingChangeDate[dateIdx] and startDate <= mappingChangeDate[(dateIdx + 1)]:
                        periodBool[dateIdx] = 1
                        startIdx = dateIdx
                    if endDate > mappingChangeDate[dateIdx] and endDate <= mappingChangeDate[(dateIdx + 1)]:
                        periodBool[dateIdx] = 1
                        endIdx = dateIdx

                if startIdx != endIdx and endIdx - startIdx > 1:
                    for fillPeriodIdx in range(endIdx - startIdx - 1):
                        periodBool[startIdx + 1 + fillPeriodIdx] = 1

                verboseprint(periodBool)
                findMap = 0
                if mappingFileName.find('HV') != -1:
                    verboseprint('You are using a HV map')
                    findMap = 1
                    mappingLength = 504
                    if sliceTestFlag == 1:
                        mappingLength = 14
                if mappingFileName.find('LV') != -1:
                    verboseprint('You are using a LV map')
                    findMap = -1
                    mappingLength = 144
                    if sliceTestFlag == 1:
                        mappingLength = 12
                ExistingChambers = []
                nExistingChambers = sum(1 for line in open(existingChambersFileName))
                verboseprint('In ' + existingChambersFileName + ' you have ' + str(nExistingChambers) + ' chambers')
                fileExChambers = open(existingChambersFileName, 'r')
                fileExChambersLine = fileExChambers.readlines()
                for exChamber in range(int(nExistingChambers)):
                    exChamberName = str(fileExChambersLine[exChamber])[:-1]
                    ShortAliasOneChamber = exChamberName.split(':')
                    ExistingChambers.append(ShortAliasOneChamber)

                verboseprint('ExistingChambers:', ExistingChambers)
                howManyChambers = sum(1 for line in open(chambersFileName))
                verboseprint('In ' + chambersFileName + ' you have ' + str(howManyChambers) + ' chambers')
                fileChambers = open(chambersFileName, 'r')
                fileChambersLine = fileChambers.readlines()
                chamberList = []
                for chIdx in range(int(howManyChambers)):
                    chamberName = str(fileChambersLine[chIdx])[:-1]
                    ExistBool = False
                    for existIdx in range(len(ExistingChambers)):
                        for existSplitIdx in range(len(ExistingChambers[existIdx])):
                            alterName = ExistingChambers[existIdx][existSplitIdx]
                            if chamberName == alterName:
                                ExistBool = True

                    if ExistBool == False:
                        print('ERROR: WRONG NAME OF THE CHAMBER: the accepted names are in File: ' + existingChambersFileName)
                        return 1
                    chamberList.append(chamberName)

                verboseprint(chamberList)
                fileMapping = open(mappingFileName, 'r')
                fileMappingLine = fileMapping.readlines()
                startMappingLines = []
                boolMapping = []
                for i in range(len(periodBool)):
                    boolMapping.append(False)

            lineCounter = 0
            for x in fileMappingLine:
                columnIdx = x.index(':')
                for mapIdx in range(len(boolMapping)):
                    if str(x)[:columnIdx] == 'Mapping' + str(mapIdx + 1):
                        boolMapping[mapIdx] = True
                        startMappingLines.append(int(fileMappingLine.index(x)))

                lineCounter = lineCounter + 1

        allCorrectMapFlag = True
        for mapIdx in range(len(boolMapping)):
            if boolMapping[mapIdx] == False:
                allCorrectMapFlag = False
                print('ERROR: Map ' + str(mapIdx + 1) + ' not charged correctely')
                return 1

    if allCorrectMapFlag == True:
        for mapIdx in range(len(boolMapping)):
            boolMapping[mapIdx] = bool(periodBool[mapIdx])

    if boolMapping != periodBool:
        print('ERROR: boolMapping != periodBool')
        return 1
    else:
        column1 = fileMappingLine[0].index(':')
        subString1 = fileMappingLine[0][column1 + 1:]
        column2 = subString1.index(':')
        stringFrontDP = subString1[column2 + 2:-2]
        allMappingList = []
        for idxMap in range(len(boolMapping)):
            oneMap = []
            for lineIdx in range(startMappingLines[idxMap] + 1, startMappingLines[idxMap] + 1 + mappingLength):
                oneMap.append(stringFrontDP + fileMappingLine[lineIdx][:-1])

            allMappingList.append(oneMap)

        db = cx_Oracle.connect(dbAccount + dbName)
        cur = db.cursor()
        AllChosenChamberAllDPsWanted = []
        for chIdx in range(len(chamberList)):
            OneChamberAllDPs = []
            for allMapIdx in range(len(allMappingList)):
                OneMapAllDPs = []
                for oneMapIdx in range(len(allMappingList[allMapIdx])):
                    oneMapLine = allMappingList[allMapIdx][oneMapIdx]
                    if monitorFlag == 'HV':
                        if sliceTestFlag == 0:
                            channelNameAsInMap = [
                             'G3Bot', 'G3Top', 'G2Bot', 'G2Top', 'G1Bot', 'G1Top', 'Drift']
                        if sliceTestFlag == 1:
                            channelNameAsInMap = [
                             'G3bot', 'G3top', 'G2bot', 'G2top', 'G1bot', 'G1top', 'Drift']
                    if monitorFlag == 'LV':
                        if sliceTestFlag == 0:
                            channelNameAsInMap = [
                             'L1', 'L2']
                        if sliceTestFlag == 1:
                            if allMapIdx == 0:
                                channelNameAsInMap = [
                                 'TOP_VFAT', 'TOP_OH2V', 'TOP_OH4V', 'BOT_VFAT', 'BOT_OH2V', 'BOT_OH4V']
                            if allMapIdx == 1:
                                channelNameAsInMap = [
                                 'L1_VFAT', 'L1_OH2V', 'L1_OH4V', 'L2_VFAT', 'L2_OH2V', 'L2_OH4V']
                    for channelNameIdx in range(len(channelNameAsInMap)):
                        if oneMapLine.find(channelNameAsInMap[channelNameIdx]) != -1:
                            chamberMatch = False
                            for existChamberIdx in range(len(ExistingChambers)):
                                listAlterNamesOneChamber = ExistingChambers[existChamberIdx]
                                for alterNamesIdx in range(len(listAlterNamesOneChamber)):
                                    if chamberList[chIdx] == listAlterNamesOneChamber[alterNamesIdx]:
                                        chamberMatch = True
                                        indexInExistingChambers = existChamberIdx

                            for alterNameThisChamberIdx in range(len(ExistingChambers[indexInExistingChambers])):
                                alterName = ExistingChambers[indexInExistingChambers][alterNameThisChamberIdx]
                                if oneMapLine.find(alterName) != -1:
                                    column2Idx = oneMapLine.index(':', 15)
                                    OneChannelOneDP = oneMapLine[:column2Idx]
                                    OneChannelMapAlias = oneMapLine[column2Idx + 1:]
                                    OneChannelOneShortAlias = alterName
                                    verboseprint('PairDPAlias', OneChannelOneDP, OneChannelOneShortAlias)
                                    query = "select SINCE, DPE_NAME, ALIAS from CMS_GEM_PVSS_COND.ALIASES where DPE_NAME='" + str(OneChannelOneDP) + ".' and ALIAS='" + str(OneChannelMapAlias) + "'"
                                    cur.execute(query)
                                    curALIAS = cur
                                    boolNoSinceSeen = True
                                    for result in curALIAS:
                                        boolNoSinceSeen = False
                                        OneChannelOneSince = result[0]

                                    if boolNoSinceSeen:
                                        OneChannelOneSince = datetime(1970, 1, 1, 0, 0, 1)
                                    DPAliasSinceOneChannel = []
                                    DPAliasSinceOneChannel.append(OneChannelOneDP)
                                    DPAliasSinceOneChannel.append(OneChannelOneShortAlias)
                                    DPAliasSinceOneChannel.append(OneChannelOneSince)
                                    OneMapAllDPs.append(DPAliasSinceOneChannel)

                OneChamberAllDPs.append(OneMapAllDPs)

            howManyChannelsInAMap = len(OneChamberAllDPs[0])
            OneChamberAllDPsWanted = []
            for channelIdx in range(howManyChannelsInAMap):
                fixedChannelList = []
                for mapIdx in range(len(OneChamberAllDPs)):
                    takenTriplet = OneChamberAllDPs[mapIdx][channelIdx]
                    fixedChannelList.append(takenTriplet)

                OneChamberAllDPsWanted.append(fixedChannelList)

            for channelIdx in range(len(OneChamberAllDPsWanted)):
                OneChannelAllMapsList = OneChamberAllDPsWanted[channelIdx]
                OneChannelAllMapsListSorted = sorted(OneChannelAllMapsList, key=lambda element: element[2])
                OneChamberAllDPsWanted[channelIdx] = OneChannelAllMapsListSorted

            for channelIdx in range(len(OneChamberAllDPsWanted)):
                listOfDates = []
                for mapIdx in range(len(OneChamberAllDPsWanted[channelIdx])):
                    usedMap = False
                    sinceMap = OneChamberAllDPsWanted[channelIdx][mapIdx][2]
                    verboseprint('sinceMap', sinceMap)
                    pairDateFalse = []
                    pairDateFalse.append(sinceMap)
                    pairDateFalse.append(False)
                    listOfDates.append(pairDateFalse)

                startPair = [startDate, True]
                endPair = [endDate, True]
                listOfDates.append(startPair)
                listOfDates.append(endPair)
                sortDates = sorted(listOfDates, key=lambda element: element[0])
                startIdx = sortDates.index(startPair)
                endIdx = sortDates.index(endPair)
                if startIdx == 0:
                    verboseprint('start is before the first since')
                if startIdx == 0 and endIdx == 1:
                    verboseprint('both start and end are before the first since: no data expected')
                if startIdx != 0:
                    sortDates[(startIdx - 1)][1] = True
                for sortIdx in range(len(sortDates)):
                    if sortIdx > startIdx and sortIdx < endIdx:
                        sortDates[sortIdx][1] = True

                verboseprint('sortDates', sortDates)
                verboseprint('OneChamberAllDPsWanted', OneChamberAllDPsWanted[channelIdx][mapIdx])
                for mapIdx in range(len(OneChamberAllDPsWanted[channelIdx])):
                    sinceDate = OneChamberAllDPsWanted[channelIdx][mapIdx][2]
                    threeElements = OneChamberAllDPsWanted[channelIdx][mapIdx]
                    for sortIdx in range(len(sortDates)):
                        if sortDates[sortIdx][0] == OneChamberAllDPsWanted[channelIdx][mapIdx][2]:
                            verboseprint('sortDate: ', sortDates[sortIdx][1])
                            threeElements.append(sortDates[sortIdx][1])
                            OneChamberAllDPsWanted[channelIdx][mapIdx] = threeElements

            verboseprint('OneChamberAllDPsWanted with true or false', OneChamberAllDPsWanted)
            verboseprint('-------------------------------------------------------------------------------------------------------------------------')
            verboseprint('                    ' + chamberList[chIdx] + ' :CALLED DPs AND THEIR IDs')
            for channelIdx in range(len(OneChamberAllDPsWanted)):
                oneChannelIDs = []
                for mapIdx in range(len(OneChamberAllDPsWanted[channelIdx])):
                    thisMapDP = OneChamberAllDPsWanted[channelIdx][mapIdx][0]
                    thisMapAlias = OneChamberAllDPsWanted[channelIdx][mapIdx][1]
                    query = "select ID, DPNAME from CMS_GEM_PVSS_COND.DP_NAME2ID where DPNAME='" + thisMapDP + "'"
                    cur.execute(query)
                    curID = cur
                    for result in curID:
                        dpID = result[0]
                        dpNAME = result[1]

                    verboseprint('chamber:', chamberList[chIdx], 'channel', channelNameAsInMap[channelIdx], 'ID', dpID, 'DPNAME', dpNAME, 'ALIAS', thisMapAlias)
                    fourElements = OneChamberAllDPsWanted[channelIdx][mapIdx]
                    fourElements.append(dpID)
                    OneChamberAllDPsWanted[channelIdx][mapIdx] = fourElements

            verboseprint('OneChamberAllDPsWanted with also IDs', OneChamberAllDPsWanted)
            AllChosenChamberAllDPsWanted.append(OneChamberAllDPsWanted)

        if monitorFlag == 'HV':
            tableData = 'CMS_GEM_PVSS_COND.FWCAENCHANNELA1515'
        if monitorFlag == 'LV':
            tableData = 'CMS_GEM_PVSS_COND.FWCAENCHANNEL'
        stringWhatRetriveList = ['imon', 'vmon', 'smon', 'ison', 'temp']
        for chIdx in range(len(chamberList)):
            chamberNameRootFile = chamberList[chIdx].replace('-', '_M')
            chamberNameRootFile = chamberNameRootFile.replace('+', '_P')
            chamberNameRootFile = chamberNameRootFile.replace('/', '_')
            firstDir = f1.mkdir(chamberNameRootFile)
            firstDir.cd()
            if monitorFlag == 'HV':
                if sliceTestFlag == 0:
                    channelName = [
                     'G3Bot', 'G3Top', 'G2Bot', 'G2Top', 'G1Bot', 'G1Top', 'Drift']
                if sliceTestFlag == 1:
                    channelName = [
                     'G3Bot', 'G3Top', 'G2Bot', 'G2Top', 'G1Bot', 'G1Top', 'Drift']
            if monitorFlag == 'LV':
                if sliceTestFlag == 0:
                    channelName = [
                     'L1', 'L2']
                if sliceTestFlag == 1:
                    channelName = [
                     'L1_VFAT', 'L1_OH2V', 'L1_OH4V', 'L2_VFAT', 'L2_OH2V', 'L2_OH4V']
            Imontmultig1 = ROOT.TMultiGraph()
            titleMultig1 = chamberList[chIdx] + '; ;Imon (#mu A)'
            if monitorFlag == 'LV':
                titleMultig1 = chamberList[chIdx] + '; ;Imon (A)'
            Imontmultig1.SetName(chamberList[chIdx] + '_Imon_AllChannels')
            Imontmultig1.SetTitle(titleMultig1)
            minDateImonMultig = 9999999
            maxDateImonMultig = 1
            minValImonMultig = 999999
            maxValImonMultig = -999999
            Vmontmultig1 = ROOT.TMultiGraph()
            titleMultig1 = chamberList[chIdx] + '; ;#Delta Vmon (V)'
            Vmontmultig1.SetName(chamberList[chIdx] + '_Vmon_AllChannels')
            Vmontmultig1.SetTitle(titleMultig1)
            minDateVmonMultig = 999999
            maxDateVmonMultig = 1
            minValVmonMultig = 999999
            maxValVmonMultig = -999999
            Smontmultig1 = ROOT.TMultiGraph()
            titleMultig1 = chamberList[chIdx] + '; ;Status code'
            Smontmultig1.SetName(chamberList[chIdx] + '_Smon_AllChannels')
            Smontmultig1.SetTitle(titleMultig1)
            minDateSmonMultig = 999999
            maxDateSmonMultig = 1
            minValSmonMultig = 999999
            maxValSmonMultig = -999999
            Isontmultig1 = ROOT.TMultiGraph()
            titleMultig1 = chamberList[chIdx] + '; ;IsOn code (0=OFF, 1=ON)'
            Isontmultig1.SetName(chamberList[chIdx] + '_Ison_AllChannels')
            Isontmultig1.SetTitle(titleMultig1)
            minDateIsonMultig = 999999
            maxDateIsonMultig = 1
            minValIsonMultig = 999999
            maxValIsonMultig = -999999
            Temptmultig1 = ROOT.TMultiGraph()
            titleMultig1 = chamberList[chIdx] + '; ;Temperature (Celsius degrees)'
            Temptmultig1.SetName(chamberList[chIdx] + '_Temp_AllChannels')
            Temptmultig1.SetTitle(titleMultig1)
            minDateTempMultig = 999999
            maxDateTempMultig = 1
            minValTempMultig = 999999
            maxValTempMultig = -999999
            legendMultiImon = ROOT.TLegend(0.55, 0.2, 0.88, 0.382)
            legendMultiImon.SetTextSize(0.025)
            legendMultiImon.SetTextFont(42)
            legendMultiVmon = ROOT.TLegend(0.55, 0.665, 0.88, 0.88)
            legendMultiVmon.SetTextSize(0.025)
            legendMultiVmon.SetTextFont(42)
            for channelIdx in range(len(AllChosenChamberAllDPsWanted[chIdx])):
                OneChannelInfo = AllChosenChamberAllDPsWanted[chIdx][channelIdx]
                imonData = []
                vmonData = []
                smonData = []
                isonData = []
                tempData = []
                howManySince = len(OneChannelInfo)
                contData = 0
                for mapIdx in range(len(OneChannelInfo)):
                    sinceThisMap = OneChannelInfo[mapIdx][2]
                    aliasThisMap = OneChannelInfo[mapIdx][1]
                    firstDateToCall = startDate
                    if sinceThisMap > startDate:
                        if OneChannelInfo[mapIdx][3]:
                            firstDateToCall = str(sinceThisMap)
                            firstDateToCall_lastColumnIdx = firstDateToCall.rfind(':')
                            firstDateToCall = firstDateToCall[:firstDateToCall_lastColumnIdx + 3]
                    lastDateToCall = endDate
                    if mapIdx != len(OneChannelInfo) - 1:
                        sinceNextMap = OneChannelInfo[(mapIdx + 1)][2]
                        if sinceNextMap < endDate:
                            if OneChannelInfo[(mapIdx + 1)][3]:
                                lastDateToCall = str(sinceNextMap)
                                lastDateToCall_lastColumnIdx = lastDateToCall.rfind(':')
                                lastDateToCall = lastDateToCall[:lastDateToCall_lastColumnIdx + 3]
                    if monitorFlag == 'HV':
                        queryAll = 'select CHANGE_DATE, ACTUAL_IMON, ACTUAL_VMON, ACTUAL_STATUS, ACTUAL_ISON, ACTUAL_TEMP, ACTUAL_IMONREAL from ' + tableData + ' where DPID = ' + str(OneChannelInfo[mapIdx][4]) + " and CHANGE_DATE > to_date( '" + str(firstDateToCall) + "', 'YYYY-MM-DD HH24:MI:SS') and CHANGE_DATE < to_date( '" + str(lastDateToCall) + "', 'YYYY-MM-DD HH24:MI:SS')"
                    if monitorFlag == 'LV':
                        queryAll = 'select CHANGE_DATE, ACTUAL_IMON, ACTUAL_VMON, ACTUAL_STATUS, ACTUAL_ISON, ACTUAL_TEMP from ' + tableData + ' where DPID = ' + str(OneChannelInfo[mapIdx][4]) + " and CHANGE_DATE > to_date( '" + str(firstDateToCall) + "', 'YYYY-MM-DD HH24:MI:SS') and CHANGE_DATE < to_date( '" + str(lastDateToCall) + "', 'YYYY-MM-DD HH24:MI:SS')"
                    verboseprint('OneChannelInfo', OneChannelInfo)
                    verboseprint('query', queryAll)
                    cur.execute(queryAll)
                    curAllData = cur
                    for result in curAllData:
                        dateElem = result[0]
                        imonElem = result[1]
                        vmonElem = result[2]
                        smonElem = result[3]
                        isonElem = result[4]
                        tempElem = result[5]
                        if monitorFlag == 'HV':
                            imonRealElem = result[6]
                        dateElemString = str(dateElem)
                        if contData == 0:
                            startTs = result[0]
                        tot_secondsDate = (dateElem - startTs).total_seconds()
                        dateElemStr = str(dateElem)
                        if dateElemStr.find('.') != -1:
                            dotIdx = dateElemStr.index('.')
                            dateNoMicro = dateElemStr[:dotIdx]
                            micro = dateElemStr[dotIdx + 1:]
                        else:
                            dateNoMicro = dateElemStr
                            micro = '000000'
                        da1 = ROOT.TDatime(dateNoMicro)
                        convertedDate = da1.Convert()
                        floatMicro = '0.' + micro
                        dateElemSQL = convertedDate + float(floatMicro)
                        if imonElem is not None:
                            tripleList = [
                             tot_secondsDate, dateElemSQL, imonElem]
                            imonData.append(tripleList)
                        if vmonElem is not None:
                            tripleList = [
                             tot_secondsDate, dateElemSQL, vmonElem, mapIdx, dateElemStr]
                            vmonData.append(tripleList)
                        if smonElem is not None:
                            tripleList = [
                             tot_secondsDate, dateElemSQL, smonElem, dateElemString]
                            if smonElem < 0:
                                continue
                            smonData.append(tripleList)
                        if isonElem is not None:
                            tripleList = [
                             tot_secondsDate, dateElemSQL, isonElem]
                            isonData.append(tripleList)
                        if tempElem is not None:
                            tripleList = [
                             tot_secondsDate, dateElemSQL, tempElem]
                            tempData.append(tripleList)
                        contData = contData + 1

                    verboseprint(chamberList[chIdx] + ' ' + channelName[channelIdx] + ' (Alias: ' + aliasThisMap + '): Not sorted lists created: WAIT PLEASE!!')
                    imonData = sorted(imonData, key=lambda element: element[0])
                    vmonData = sorted(vmonData, key=lambda element: element[0])
                    smonData = sorted(smonData, key=lambda element: element[0])
                    isonData = sorted(isonData, key=lambda element: element[0])
                    tempData = sorted(tempData, key=lambda element: element[0])
                    verboseprint('   Lists sorted: WAIT PLEASE!!')
                    fileVolts = open('Over1000Volts.txt', 'a')
                    chchBool = False
                    for vIdx in range(len(vmonData)):
                        if vmonData[vIdx][2] >= 1000:
                            stringChamberChannel = chamberList[chIdx] + '\t' + channelName[channelIdx] + '\t' + aliasThisMap + '\n'
                            stringValues = 'Date:' + str(vmonData[vIdx][4]) + '\t' + ' Vmon:' + str(vmonData[vIdx][2]) + '\n'
                            if not chchBool:
                                fileVolts.write(stringChamberChannel)
                                chchBool = True
                            fileVolts.write(stringValues)

                    fileVolts.close()

                for idxElem in range(len(imonData)):
                    secondAndThird = []
                    secondAndThird.append(imonData[idxElem][1])
                    secondAndThird.append(imonData[idxElem][2])
                    imonData[idxElem] = secondAndThird

                for idxElem in range(len(vmonData)):
                    secondAndThird = []
                    secondAndThird.append(vmonData[idxElem][1])
                    secondAndThird.append(vmonData[idxElem][2])
                    vmonData[idxElem] = secondAndThird

                for idxElem in range(len(smonData)):
                    secondAndThird = []
                    secondAndThird.append(smonData[idxElem][1])
                    secondAndThird.append(int(smonData[idxElem][2]))
                    secondAndThird.append(smonData[idxElem][3])
                    smonData[idxElem] = secondAndThird

                for idxElem in range(len(isonData)):
                    secondAndThird = []
                    secondAndThird.append(isonData[idxElem][1])
                    secondAndThird.append(isonData[idxElem][2])
                    isonData[idxElem] = secondAndThird

                for idxElem in range(len(tempData)):
                    secondAndThird = []
                    secondAndThird.append(tempData[idxElem][1])
                    secondAndThird.append(tempData[idxElem][2])
                    tempData[idxElem] = secondAndThird

                verboseprint('   Sorted lists filled!')
                if monitorFlag == 'HV':
                    IMin = -20
                    IMax = 20
                    NBinImon = int(IMax - IMin)
                    IUnitMeasure = 'I [uA]'
                    VMin = -50
                    VMax = 800
                    NBinVmon = int((VMax - VMin) / 10)
                    StatusMin = 0
                    StatusMax = 4100
                    NBinStatus = StatusMax
                    IsonMin = -1
                    IsonMax = 3
                    NBinIson = int(IsonMax - IsonMin)
                    TempMin = 0
                    TempMax = 100
                    NBinTemp = TempMax
                if monitorFlag == 'LV':
                    IMin = -10
                    IMax = 10
                    NBinImon = int(IMax - IMin)
                    IUnitMeasure = 'I [A]'
                    VMin = -10
                    VMax = 10
                    NBinVmon = int((VMax - VMin) / 10)
                    StatusMin = 0
                    StatusMax = 65536
                    NBinStatus = StatusMax
                    IsonMin = -1
                    IsonMax = 3
                    NBinIson = int(IsonMax - IsonMin)
                    TempMin = 0
                    TempMax = 100
                    NBinTemp = TempMax
                chamberNameRootFile = chamberList[chIdx].replace('-', '_M')
                chamberNameRootFile = chamberNameRootFile.replace('+', '_P')
                chamberNameRootFile = chamberNameRootFile.replace('/', '_')
                Imonh1 = ROOT.TH1F(monitorFlag + '_ImonChamber' + chamberNameRootFile + '_' + channelName[channelIdx] + '_TH1', monitorFlag + '_ImonChamber' + chamberNameRootFile + '_' + channelName[channelIdx] + '_TH1', NBinImon, IMin, IMax)
                Vmonh1 = ROOT.TH1F(monitorFlag + '_VmonChamber' + chamberNameRootFile + '_' + channelName[channelIdx] + '_TH1', monitorFlag + '_VmonChamber' + chamberNameRootFile + '_' + channelName[channelIdx] + '_TH1', NBinVmon, VMin, VMax)
                Smonh1 = ROOT.TH1F(monitorFlag + '_StatusChamber' + chamberNameRootFile + '_' + channelName[channelIdx] + '_TH1', monitorFlag + '_StatusChamber' + chamberNameRootFile + '_' + channelName[channelIdx] + '_TH1', NBinStatus, StatusMin, StatusMax)
                Isonh1 = ROOT.TH1F(monitorFlag + '_IsonChamber' + chamberNameRootFile + '_' + channelName[channelIdx] + '_TH1', monitorFlag + '_IsonChamber' + chamberNameRootFile + '_' + channelName[channelIdx] + '_TH1', NBinIson, IsonMin, IsonMax)
                Temph1 = ROOT.TH1F(monitorFlag + '_TempChamber' + chamberNameRootFile + '_' + channelName[channelIdx] + '_TH1', monitorFlag + '_TempChamber' + chamberNameRootFile + '_' + channelName[channelIdx] + '_TH1', NBinTemp, TempMin, TempMax)
                Imonh1.GetXaxis().SetTitle(IUnitMeasure)
                Imonh1.GetYaxis().SetTitle('counts')
                Vmonh1.GetXaxis().SetTitle('V [V]')
                Vmonh1.GetYaxis().SetTitle('counts')
                Smonh1.GetXaxis().SetTitle('Status code')
                Smonh1.GetYaxis().SetTitle('counts')
                Isonh1.GetXaxis().SetTitle('Ison status (0=OFF, 1=ON)')
                Isonh1.GetYaxis().SetTitle('counts')
                Temph1.GetXaxis().SetTitle('Temperature [Celsius degrees]')
                Temph1.GetYaxis().SetTitle('counts')
                for idxPoint in range(len(imonData)):
                    Imonh1.Fill(imonData[idxPoint][1])

                for idxPoint in range(len(vmonData)):
                    Vmonh1.Fill(vmonData[idxPoint][1])

                for idxPoint in range(len(smonData)):
                    Smonh1.Fill(smonData[idxPoint][1])

                for idxPoint in range(len(isonData)):
                    Isonh1.Fill(isonData[idxPoint][1])

                for idxPoint in range(len(tempData)):
                    Temph1.Fill(tempData[idxPoint][1])

                Imonh1.Write()
                Vmonh1.Write()
                Smonh1.Write()
                Isonh1.Write()
                Temph1.Write()
                imonData_dates = array('d')
                vmonData_dates = array('d')
                smonData_dates = array('d')
                isonData_dates = array('d')
                tempData_dates = array('d')
                imonData_values = array('d')
                vmonData_values = array('d')
                smonData_values = array('d')
                isonData_values = array('d')
                tempData_values = array('d')
                for imonIdx in range(len(imonData)):
                    imonData_dates.append(imonData[imonIdx][0])
                    imonData_values.append(imonData[imonIdx][1])

                for vmonIdx in range(len(vmonData)):
                    vmonData_dates.append(vmonData[vmonIdx][0])
                    vmonData_values.append(vmonData[vmonIdx][1])

                for smonIdx in range(len(smonData)):
                    smonData_dates.append(smonData[smonIdx][0])
                    smonData_values.append(smonData[smonIdx][1])

                for isonIdx in range(len(isonData)):
                    isonData_dates.append(isonData[isonIdx][0])
                    isonData_values.append(isonData[isonIdx][1])

                for tempIdx in range(len(tempData)):
                    tempData_dates.append(tempData[tempIdx][0])
                    tempData_values.append(tempData[tempIdx][1])

                dummyNumber = -999999999
                if monitorFlag == 'HV':
                    dummyStatus = 4095
                if monitorFlag == 'LV':
                    dummyStatus = 65535
                dummyDate = str('1970-01-01 00:00:01.000001')
                dummyPair = [0, dummyNumber]
                dummyThree = [0, dummyStatus, dummyDate]
                if len(vmonData) == 0 and sliceTestFlag == 0 and monitorFlag == 'HV':
                    foundLast = False
                    firstDateBackInTime = firstDateToCall
                    lastDateBackInTime = lastDateToCall
                    refDate = firstDateToCall
                    timeIntervalStep = lastDateToCall - firstDateToCall
                    for queryIdx in range(5):
                        firstDateBackInTime = refDate - timedelta(hours=12 * (queryIdx + 1))
                        lastDateBackInTime = refDate - timedelta(hours=12 * queryIdx)
                        queryLastValue = 'select CHANGE_DATE, ACTUAL_VMON from ' + tableData + ' where DPID = ' + str(OneChannelInfo[mapIdx][4]) + " and CHANGE_DATE > to_date( '" + str(firstDateBackInTime) + "', 'YYYY-MM-DD HH24:MI:SS') and CHANGE_DATE < to_date( '" + str(lastDateBackInTime) + "', 'YYYY-MM-DD HH24:MI:SS')"
                        verboseprint(queryLastValue)
                        cur.execute(queryLastValue)
                        curLast = cur
                        lastValueList = []
                        for curLastElem in curLast:
                            lastValue_date = curLastElem[0]
                            lastValue_value = curLastElem[1]
                            if lastValue_value is not None:
                                lastValueList.append([lastValue_date, lastValue_value])

                        lastValueList = sorted(lastValueList, key=lambda element: element[0])
                        if len(lastValueList) > 0:
                            lastSavedVoltage_value = lastValueList[(-1)][1]
                            foundLast = True
                            break

                    startLast = start.replace('_', '-')
                    startLastSplitList = startLast.split('-')
                    lastDateStr = startLastSplitList[0] + '-' + startLastSplitList[1] + '-' + startLastSplitList[2] + ' ' + startLastSplitList[3] + ':' + startLastSplitList[4] + ':' + startLastSplitList[5]
                    verboseprint('lastDateStr', lastDateStr)
                    last_date = ROOT.TDatime(lastDateStr)
                    lastDateConverted = last_date.Convert()
                    floatMicro_LAST = '0.000001'
                    dateElemSQL_LAST = lastDateConverted + float(floatMicro_LAST)
                if len(imonData) == 0:
                    imonData_dates.append(0)
                    imonData_values.append(dummyNumber)
                    imonData.append(dummyPair)
                if len(vmonData) == 0:
                    if foundLast:
                        vmonData_dates.append(dateElemSQL_LAST)
                        vmonData_values.append(lastSavedVoltage_value)
                        vmonData.append([dateElemSQL_LAST, lastSavedVoltage_value])
                    else:
                        vmonData_dates.append(0)
                        vmonData_values.append(dummyNumber)
                        vmonData.append(dummyPair)
                if len(smonData) == 0:
                    smonData_dates.append(0)
                    smonData_values.append(dummyStatus)
                    smonData.append(dummyThree)
                if len(isonData) == 0:
                    isonData_dates.append(0)
                    isonData_values.append(dummyNumber)
                    isonData.append(dummyPair)
                if len(tempData) == 0:
                    tempData_dates.append(0)
                    tempData_values.append(dummyNumber)
                    tempData.append(dummyPair)
                if imonData_dates[0] < minDateImonMultig:
                    minDateImonMultig = imonData_dates[0] - 1
                if imonData_dates[(-1)] > maxDateImonMultig:
                    maxDateImonMultig = imonData_dates[(-1)] + 1
                if vmonData_dates[0] < minDateVmonMultig:
                    minDateVmonMultig = vmonData_dates[0] - 1
                if vmonData_dates[(-1)] > maxDateVmonMultig:
                    maxDateVmonMultig = vmonData_dates[(-1)] + 1
                if smonData_dates[0] < minDateSmonMultig:
                    minDateSmonMultig = smonData_dates[0] - 1
                if smonData_dates[(-1)] > maxDateSmonMultig:
                    maxDateSmonMultig = smonData_dates[(-1)] + 1
                if isonData_dates[0] < minDateIsonMultig:
                    minDateIsonMultig = isonData_dates[0] - 1
                if isonData_dates[(-1)] > maxDateIsonMultig:
                    maxDateIsonMultig = isonData_dates[(-1)] + 1
                if tempData_dates[0] < minDateTempMultig:
                    minDateTempMultig = tempData_dates[0] - 1
                if tempData_dates[(-1)] > maxDateTempMultig:
                    maxDateTempMultig = tempData_dates[(-1)] + 1
                if min(imonData_values) < minValImonMultig:
                    minValImonMultig = min(imonData_values)
                if max(imonData_values) > maxValImonMultig:
                    maxValImonMultig = max(imonData_values)
                if min(vmonData_values) < minValVmonMultig:
                    minValVmonMultig = min(vmonData_values)
                if max(vmonData_values) > maxValVmonMultig:
                    maxValVmonMultig = max(vmonData_values)
                if min(smonData_values) < minValSmonMultig:
                    minValSmonMultig = min(smonData_values)
                if max(smonData_values) > maxValSmonMultig:
                    maxValSmonMultig = max(smonData_values)
                if min(tempData_values) < minValTempMultig:
                    minValTempMultig = min(tempData_values)
                if max(tempData_values) > maxValTempMultig:
                    maxValTempMultig = max(tempData_values)
                Imontg1 = ROOT.TGraph(len(imonData), imonData_dates, imonData_values)
                Vmontg1 = ROOT.TGraph(len(vmonData), vmonData_dates, vmonData_values)
                Smontg1 = ROOT.TGraph(len(smonData), smonData_dates, smonData_values)
                Isontg1 = ROOT.TGraph(len(isonData), isonData_dates, isonData_values)
                Temptg1 = ROOT.TGraph(len(tempData), tempData_dates, tempData_values)
                markColor = 4
                markNum = 20
                transWhite = ROOT.TColor.GetColorTransparent(0, 0)
                if monitorFlag == 'HV':
                    if channelName[channelIdx].find('G3Bot') != -1:
                        markColor = 1
                        markNum = 20
                    if channelName[channelIdx].find('G3Top') != -1:
                        markColor = 2
                        markNum = 21
                    if channelName[channelIdx].find('G2Bot') != -1:
                        markColor = 3
                        markNum = 22
                    if channelName[channelIdx].find('G2Top') != -1:
                        markColor = 4
                        markNum = 23
                    if channelName[channelIdx].find('G1Bot') != -1:
                        markColor = 6
                        markNum = 29
                    if channelName[channelIdx].find('G1Top') != -1:
                        markColor = 7
                        markNum = 33
                    if channelName[channelIdx].find('Drift') != -1:
                        markColor = 401
                        markNum = 34
                if monitorFlag == 'LV':
                    if channelName[channelIdx].find('L1') != -1:
                        markColor = 2
                        markNum = 20
                    if channelName[channelIdx].find('L2') != -1:
                        markColor = 4
                        markNum = 21
                Imontg1.SetLineWidth(0)
                Imontg1.SetMarkerColor(markColor)
                Imontg1.SetMarkerStyle(markNum)
                Imontg1.SetMarkerSize(1)
                Vmontg1.SetLineWidth(0)
                Vmontg1.SetMarkerColor(markColor)
                Vmontg1.SetMarkerStyle(markNum)
                Vmontg1.SetMarkerSize(1)
                Smontg1.SetLineWidth(0)
                Smontg1.SetMarkerColor(markColor)
                Smontg1.SetMarkerStyle(markNum)
                Smontg1.SetMarkerSize(1)
                Isontg1.SetLineWidth(0)
                Isontg1.SetMarkerColor(markColor)
                Isontg1.SetMarkerStyle(markNum)
                Isontg1.SetMarkerSize(1)
                Temptg1.SetLineWidth(0)
                Temptg1.SetMarkerColor(markColor)
                Temptg1.SetMarkerStyle(markNum)
                Temptg1.SetMarkerSize(1)
                Imontg1.SetName(monitorFlag + '_ImonChamber' + chamberNameRootFile + '_' + channelName[channelIdx] + '_UTC_time')
                Vmontg1.SetName(monitorFlag + '_VmonChamber' + chamberNameRootFile + '_' + channelName[channelIdx] + '_UTC_time')
                Smontg1.SetName(monitorFlag + '_StatusChamber' + chamberNameRootFile + '_' + channelName[channelIdx] + '_UTC_time')
                Isontg1.SetName(monitorFlag + '_IsonChamber' + chamberNameRootFile + '_' + channelName[channelIdx] + '_UTC_time')
                Temptg1.SetName(monitorFlag + '_TempChamber' + chamberNameRootFile + '_' + channelName[channelIdx] + '_UTC_time')
                Imontg1.SetTitle(monitorFlag + '_ImonChamber' + chamberNameRootFile + '_' + channelName[channelIdx] + '_UTC_time')
                Vmontg1.SetTitle(monitorFlag + '_VmonChamber' + chamberNameRootFile + '_' + channelName[channelIdx] + '_UTC_time')
                Smontg1.SetTitle(monitorFlag + '_StatusChamber' + chamberNameRootFile + '_' + channelName[channelIdx] + '_UTC_time')
                Isontg1.SetTitle(monitorFlag + '_IsonChamber' + chamberNameRootFile + '_' + channelName[channelIdx] + '_UTC_time')
                Temptg1.SetTitle(monitorFlag + '_TempChamber' + chamberNameRootFile + '_' + channelName[channelIdx] + '_UTC_time')
                if monitorFlag == 'HV':
                    currentBrak = '[uA]'
                if monitorFlag == 'LV':
                    currentBrak = '[A]'
                Imontg1.GetYaxis().SetTitle('Imon ' + chamberNameRootFile + ' ' + channelName[channelIdx] + ' ' + currentBrak)
                Vmontg1.GetYaxis().SetTitle('#Delta Vmon [V]')
                Smontg1.GetYaxis().SetTitle('Status code ' + chamberNameRootFile + ' ' + channelName[channelIdx])
                Isontg1.GetYaxis().SetTitle('Ison code: 0=ON 1=OFF ' + chamberNameRootFile + ' ' + channelName[channelIdx])
                Temptg1.GetYaxis().SetTitle('Temperature ' + chamberNameRootFile + ' ' + channelName[channelIdx] + ' [Celsius degrees]')
                Imontg1.GetXaxis().SetTimeDisplay(1)
                Vmontg1.GetXaxis().SetTimeDisplay(1)
                Smontg1.GetXaxis().SetTimeDisplay(1)
                Isontg1.GetXaxis().SetTimeDisplay(1)
                Temptg1.GetXaxis().SetTimeDisplay(1)
                Imontg1.GetXaxis().SetTimeFormat('#splitline{%y-%m-%d}{%H:%M:%S}%F1970-01-01 00:00:00')
                Vmontg1.GetXaxis().SetTimeFormat('#splitline{%y-%m-%d}{%H:%M:%S}%F1970-01-01 00:00:00')
                Smontg1.GetXaxis().SetTimeFormat('#splitline{%y-%m-%d}{%H:%M:%S}%F1970-01-01 00:00:00')
                Isontg1.GetXaxis().SetTimeFormat('#splitline{%y-%m-%d}{%H:%M:%S}%F1970-01-01 00:00:00')
                Temptg1.GetXaxis().SetTimeFormat('#splitline{%y-%m-%d}{%H:%M:%S}%F1970-01-01 00:00:00')
                Imontg1.GetXaxis().SetLabelOffset(0.025)
                Vmontg1.GetXaxis().SetLabelOffset(0.025)
                Smontg1.GetXaxis().SetLabelOffset(0.025)
                Isontg1.GetXaxis().SetLabelOffset(0.025)
                Temptg1.GetXaxis().SetLabelOffset(0.025)
                Imontg1.GetXaxis().SetLabelSize(0.018)
                Vmontg1.GetXaxis().SetLabelSize(0.018)
                Smontg1.GetXaxis().SetLabelSize(0.018)
                Isontg1.GetXaxis().SetLabelSize(0.018)
                Temptg1.GetXaxis().SetLabelSize(0.018)
                Imontg1.GetYaxis().SetLabelSize(0.018)
                Vmontg1.GetYaxis().SetLabelSize(0.018)
                Smontg1.GetYaxis().SetLabelSize(0.018)
                Isontg1.GetYaxis().SetLabelSize(0.018)
                Temptg1.GetYaxis().SetLabelSize(0.018)
                Imontg1.Write()
                Vmontg1.Write()
                Smontg1.Write()
                Isontg1.Write()
                Temptg1.Write()
                canW = 800
                canH = 800
                canH_ref = 800
                canW_ref = 800
                TopMar = 0.12 * canH_ref
                BotMar = 0.17 * canH_ref
                LeftMar = 0.15 * canW_ref
                RightMar = 0.12 * canW_ref
                cmsPrelOneGr = ROOT.TPaveText(0.13, 0.88, 0.355, 0.96, 'brNDC')
                cmsPrelOneGr.AddText('CMS Preliminary')
                cmsPrelOneGr.SetTextAlign(12)
                cmsPrelOneGr.SetShadowColor(transWhite)
                cmsPrelOneGr.SetFillColor(transWhite)
                cmsPrelOneGr.SetLineColor(transWhite)
                cmsPrelOneGr.SetLineColor(transWhite)
                xAxisLabOneGr = ROOT.TPaveText(0.6, 0.88, 0.9, 0.92, 'brNDC')
                xAxisLabOneGr.AddText('Date(YY-MM-DD) / UTC Time(hh:mm:ss)')
                xAxisLabOneGr.SetTextAlign(12)
                xAxisLabOneGr.SetShadowColor(transWhite)
                xAxisLabOneGr.SetFillColor(transWhite)
                xAxisLabOneGr.SetLineColor(transWhite)
                xAxisLabOneGr.SetLineColor(transWhite)
                Imontmultig1.Add(Imontg1)
                Vmontmultig1.Add(Vmontg1)
                Smontmultig1.Add(Smontg1)
                Isontmultig1.Add(Isontg1)
                Temptmultig1.Add(Temptg1)
                if channelName[channelIdx] == 'G3Bot':
                    legendMultiImon.AddEntry(Imontg1, 'GEM-3 bot electrode', 'p')
                    legendMultiVmon.AddEntry(Imontg1, '#Delta V Induction gap', 'p')
                if channelName[channelIdx] == 'G3Top':
                    legendMultiImon.AddEntry(Imontg1, 'GEM-3 top electrode', 'p')
                    legendMultiVmon.AddEntry(Imontg1, '#Delta V GEM-3 foil', 'p')
                if channelName[channelIdx] == 'G2Bot':
                    legendMultiImon.AddEntry(Imontg1, 'GEM-2 bot electrode', 'p')
                    legendMultiVmon.AddEntry(Imontg1, '#Delta V Transfer-2 gap', 'p')
                if channelName[channelIdx] == 'G2Top':
                    legendMultiImon.AddEntry(Imontg1, 'GEM-2 top electrode', 'p')
                    legendMultiVmon.AddEntry(Imontg1, '#Delta V GEM-2 foil', 'p')
                if channelName[channelIdx] == 'G1Bot':
                    legendMultiImon.AddEntry(Imontg1, 'GEM-1 bot electrode', 'p')
                    legendMultiVmon.AddEntry(Imontg1, '#Delta V Transfer-1 gap', 'p')
                if channelName[channelIdx] == 'G1Top':
                    legendMultiImon.AddEntry(Imontg1, 'GEM-1 top electrode', 'p')
                    legendMultiVmon.AddEntry(Imontg1, '#Delta V GEM-1 foil', 'p')
                if channelName[channelIdx] == 'Drift':
                    legendMultiImon.AddEntry(Imontg1, 'Drift electrode', 'p')
                    legendMultiVmon.AddEntry(Imontg1, '#Delta V Drift gap', 'p')
                if channelName[channelIdx] == 'L1':
                    legendMultiImon.AddEntry(Imontg1, 'Layer 1', 'p')
                    legendMultiVmon.AddEntry(Imontg1, 'Layer 1', 'p')
                if channelName[channelIdx] == 'L2':
                    legendMultiImon.AddEntry(Imontg1, 'Layer 2', 'p')
                    legendMultiVmon.AddEntry(Imontg1, 'Layer 2', 'p')
                smonData_binStatus = []
                smonData_decimalStatus = []
                smonData_dateString = []
                smonData_meaningString = []
                if monitorFlag == 'HV':
                    nBit = 12
                    for smonIdx in range(len(smonData)):
                        binStat = bin(int(smonData[smonIdx][1]))[2:]
                        lenStat = len(binStat)
                        binStat = str(0) * (nBit - lenStat) + binStat
                        binStat = '0b' + binStat
                        smonData_binStatus.append(binStat)
                        smonData_decimalStatus.append(smonData[smonIdx][1])
                        smonData_dateString.append(smonData[smonIdx][2])
                        extensibleStat = ''
                        if binStat == '0b000000000000':
                            StatusMeaning = 'OFF'
                        if binStat == '0b000000000001':
                            StatusMeaning = 'ON'
                        cutBinStr = binStat[13:]
                        if cutBinStr == '0':
                            extensibleStat = extensibleStat + 'OFF' + ' '
                        else:
                            if cutBinStr == '1':
                                extensibleStat = extensibleStat + 'ON' + ' '
                            shift2 = binStat[:-1]
                            if len(shift2) != 13:
                                print('ERROR: ' + monitorFlag + ' error in len of shift2. Len=' + str(len(shift2)) + '/13')
                                print(('binStat:', binStat, 'shift2:', shift2))
                                return 1
                            if int(shift2[11:]) > 0:
                                cutBinStr = shift2[11:]
                                if cutBinStr[1] == '1':
                                    StatusMeaning = 'RUP'
                                    extensibleStat = extensibleStat + StatusMeaning + ' '
                                if cutBinStr[0] == '1':
                                    StatusMeaning = 'RDW'
                                    extensibleStat = extensibleStat + StatusMeaning + ' '
                            shift3 = binStat[:-3]
                            if len(shift3) != 11:
                                print('ERROR: ' + monitorFlag + ' error in len of shift3. Len=' + str(len(shift3)) + '/11')
                                print(('shift3:', shift3))
                                return 1
                            if int(shift3[8:]) > 0:
                                cutBinStr = shift3[8:]
                                if cutBinStr[2] == '1':
                                    StatusMeaning = 'OVC'
                                    extensibleStat = extensibleStat + StatusMeaning + ' '
                                if cutBinStr[1] == '1':
                                    StatusMeaning = 'OVV'
                                    extensibleStat = extensibleStat + StatusMeaning + ' '
                                if cutBinStr[0] == '1':
                                    StatusMeaning = 'UVV'
                                    extensibleStat = extensibleStat + StatusMeaning + ' '
                            shift4 = binStat[:-6]
                            if len(shift4) != 8:
                                print('ERROR: ' + monitorFlag + ' error in len of shift4. Len=' + str(len(shift4)) + '/8')
                                print(('shift4:', shift4))
                                return 1
                            if int(shift4[4:]) > 0:
                                cutBinStr = shift4[4:]
                                if cutBinStr[3] == '1':
                                    StatusMeaning = 'Ext Trip'
                                    extensibleStat = extensibleStat + StatusMeaning + ' '
                                if cutBinStr[2] == '1':
                                    StatusMeaning = 'Max V'
                                    extensibleStat = extensibleStat + StatusMeaning + ' '
                                if cutBinStr[1] == '1':
                                    StatusMeaning = 'Ext Disable'
                                    extensibleStat = extensibleStat + StatusMeaning + ' '
                                if cutBinStr[0] == '1':
                                    StatusMeaning = 'Int Trip'
                                    extensibleStat = extensibleStat + StatusMeaning + ' '
                            shift5 = binStat[:-10]
                            if len(shift5) != 4:
                                print('ERROR: ' + monitorFlag + ' error in len of shift5. Len=' + str(len(shift5)) + '/4')
                                print(('shift5:', shift5))
                                return 1
                            if int(shift5[3:]) > 0:
                                cutBinStr = shift5[3:]
                                if cutBinStr[0] == '1':
                                    StatusMeaning = 'Calib Error'
                                    extensibleStat = extensibleStat + StatusMeaning + ' '
                            shift6 = binStat[:-11]
                            if len(shift6) != 3:
                                print('ERROR: ' + monitorFlag + ' error in len of shift6. Len=' + str(len(shift6)) + '/3')
                                print(('shift6:', shift6))
                                return 1
                        if int(shift6[2:]) > 0:
                            cutBinStr = shift6[2:]
                            if cutBinStr[0] == '1':
                                StatusMeaning = 'Unplugged'
                                extensibleStat = extensibleStat + StatusMeaning + ' '
                        smonData_meaningString.append(extensibleStat)

                if monitorFlag == 'LV':
                    nBit = 16
                    for smonIdx in range(len(smonData)):
                        binStat = bin(int(smonData[smonIdx][1]))[2:]
                        lenStat = len(binStat)
                        binStat = str(0) * (nBit - lenStat) + binStat
                        binStat = '0b' + binStat
                        smonData_binStatus.append(binStat)
                        smonData_decimalStatus.append(smonData[smonIdx][1])
                        smonData_dateString.append(smonData[smonIdx][2])
                        extensibleStat = ''
                        if len(binStat) != nBit + 2:
                            print('ERROR: ' + monitorFlag + ' error in len of binStat. Len=' + len(binStat) + '/' + str(nBit + 2))
                            return 1
                        if binStat == '0b0000000000000000':
                            StatusMeaning = 'OFF'
                        if binStat == '0b0000000000000001':
                            StatusMeaning = 'ON'
                        cutBinStr = binStat[-1:]
                        if cutBinStr == '0':
                            extensibleStat = extensibleStat + 'OFF' + ' '
                        else:
                            if cutBinStr == '1':
                                extensibleStat = extensibleStat + 'ON' + ' '
                            removedBits = -1
                            shift2 = binStat[:removedBits]
                            if len(shift2) != nBit + 2 + removedBits:
                                print('ERROR: ' + monitorFlag + ' error in len of shift2. Len=' + len(shift2) + '/' + str(nBit + 2 + removedBits))
                                return 1
                            removedBits = removedBits - 2
                            shift3 = binStat[:removedBits]
                            if len(shift3) != nBit + 2 + removedBits:
                                print('ERROR: ' + monitorFlag + ' error in len of shift3. Len=' + len(shift3) + '/' + str(nBit + 2 + removedBits))
                                return 1
                            if int(shift3[len(shift3) - 3:]) > 0:
                                cutBinStr = shift3[len(shift3) - 3:]
                                if cutBinStr[2] == '1':
                                    StatusMeaning = 'OVC'
                                    extensibleStat = extensibleStat + StatusMeaning + ' '
                                if cutBinStr[1] == '1':
                                    StatusMeaning = 'OVV'
                                    extensibleStat = extensibleStat + StatusMeaning + ' '
                                if cutBinStr[0] == '1':
                                    StatusMeaning = 'UVV'
                                    extensibleStat = extensibleStat + StatusMeaning + ' '
                            removedBits = removedBits - 3
                            shift4 = binStat[:removedBits]
                            if len(shift4) != nBit + 2 + removedBits:
                                print('ERROR: ' + monitorFlag + ' error in len of shift4. Len=' + len(shift4) + '/' + str(nBit + 2 + removedBits))
                                return 1
                            removedBits = removedBits - 1
                            shift5 = binStat[:removedBits]
                            if len(shift5) != nBit + 2 + removedBits:
                                print('ERROR: ' + monitorFlag + ' error in len of shift5. Len=' + len(shift5) + '/' + str(nBit + 2 + removedBits))
                                return 1
                            if int(shift5[len(shift5) - 3:]) > 0:
                                cutBinStr = shift5[len(shift5) - 3:]
                                if cutBinStr[2] == '1':
                                    StatusMeaning = 'OHVMax'
                                    extensibleStat = extensibleStat + StatusMeaning + ' '
                                if cutBinStr[0] == '1':
                                    StatusMeaning = 'InTrip'
                                    extensibleStat = extensibleStat + StatusMeaning + ' '
                            removedBits = removedBits - 3
                            shift6 = binStat[:removedBits]
                            if len(shift6) != nBit + 2 + removedBits:
                                print('ERROR: ' + monitorFlag + ' error in len of shift6. Len=' + len(shift6) + '/' + str(nBit + 2 + removedBits))
                                return 1
                            if int(shift6[len(shift6) - 1:]) > 0:
                                cutBinStr = shift6[len(shift6) - 1:]
                                if cutBinStr[0] == '1':
                                    StatusMeaning = 'CalibERR'
                                    extensibleStat = extensibleStat + StatusMeaning + ' '
                            removedBits = removedBits - 1
                            shift7 = binStat[:removedBits]
                            if len(shift7) != nBit + 2 + removedBits:
                                print('ERROR: ' + monitorFlag + ' error in len of shift7. Len=' + len(shift7) + '/' + str(nBit + 2 + removedBits))
                                return 1
                            if int(shift7[len(shift7) - 1:]) > 0:
                                cutBinStr = shift7[len(shift7) - 1:]
                                if cutBinStr[0] == '1':
                                    StatusMeaning = 'Unplugged'
                                    extensibleStat = extensibleStat + StatusMeaning + ' '
                            removedBits = removedBits - 1
                            shift8 = binStat[:removedBits]
                            if len(shift8) != nBit + 2 + removedBits:
                                print('ERROR: ' + monitorFlag + ' error in len of shift8. Len=' + len(shift8) + '/' + str(nBit + 2 + removedBits))
                                return 1
                            removedBits = removedBits - 1
                            shift9 = binStat[:removedBits]
                            if len(shift9) != nBit + 2 + removedBits:
                                print('ERROR: ' + monitorFlag + ' error in len of shift9. Len=' + len(shift9) + '/' + str(nBit + 2 + removedBits))
                                return 1
                            if int(shift9[len(shift9) - 1:]) > 0:
                                cutBinStr = shift9[len(shift9) - 1:]
                                if cutBinStr[0] == '1':
                                    StatusMeaning = 'OVVPROT'
                                    extensibleStat = extensibleStat + StatusMeaning + ' '
                            removedBits = removedBits - 1
                            shift10 = binStat[:removedBits]
                            if len(shift10) != nBit + 2 + removedBits:
                                print('ERROR: ' + monitorFlag + ' error in len of shift10. Len=' + len(shift10) + '/' + str(nBit + 2 + removedBits))
                                return 1
                            if int(shift10[len(shift10) - 1:]) > 0:
                                cutBinStr = shift10[len(shift10) - 1:]
                                if cutBinStr[0] == '1':
                                    StatusMeaning = 'POWFAIL'
                                    extensibleStat = extensibleStat + StatusMeaning + ' '
                            removedBits = removedBits - 1
                            shift11 = binStat[:removedBits]
                            if len(shift11) != nBit + 2 + removedBits:
                                print('ERROR: ' + monitorFlag + ' error in len of shift11. Len=' + len(shift11) + '/' + str(nBit + 2 + removedBits))
                                return 1
                        if int(shift11[len(shift11) - 1:]) > 0:
                            cutBinStr = shift11[len(shift11) - 1:]
                            if cutBinStr[0] == '1':
                                StatusMeaning = 'TEMPERR'
                                extensibleStat = extensibleStat + StatusMeaning + ' '
                        smonData_meaningString.append(extensibleStat)

                if len(smonData) != len(smonData_binStatus):
                    print('ERROR: ' + monitorFlag + ' len(smonData) different from len(smonData_binStatus)')
                    print(('len(smonData):', len(smonData), 'len(smonData_binStatus):', len(smonData_binStatus)))
                    return 1
                if len(smonData_binStatus) != len(smonData_decimalStatus):
                    print('ERROR: ' + monitorFlag + ' len(smonData_binStatus) different from len(smonData_binStatus)')
                    print(('len(smonData_binStatus):', len(smonData_binStatus), 'len(smonData_decimalStatus):', len(smonData_decimalStatus)))
                    return 1
                if len(smonData_decimalStatus) != len(smonData_dateString):
                    print('ERROR: ' + monitorFlag + ' len(smonData_decimalStatus) different from len(smonData_dateString)')
                    print(('len(smonData_decimalStatus):', len(smonData_decimalStatus), 'len(smonData_dateString):', len(smonData_dateString)))
                    return 1
                if len(smonData_dateString) != len(smonData_meaningString):
                    print('ERROR: ' + monitorFlag + ' len(smonData_dateString) different from len(smonData_meaningString)')
                    print(('len(smonData_dateString):', len(smonData_dateString), 'len(smonData_meaningString):', len(smonData_meaningString)))
                    return 1
                StatusTree = ROOT.TTree(monitorFlag + '_StatusTree' + chamberNameRootFile + '_' + channelName[channelIdx], monitorFlag + '_StatusTree' + chamberNameRootFile + '_' + channelName[channelIdx])
                smonRootTimesDate = ROOT.vector('string')()
                smonRootDecimalStat = ROOT.vector('string')()
                smonRootBinStat = ROOT.vector('string')()
                smonRootMeaningStat = ROOT.vector('string')()
                StatusTree.Branch('TS', smonRootTimesDate)
                StatusTree.Branch('DecimalStat', smonRootDecimalStat)
                StatusTree.Branch('BinaryStat', smonRootBinStat)
                StatusTree.Branch('MeaningStat', smonRootMeaningStat)
                for smonIdx in range(len(smonData)):
                    smonRootTimesDate.push_back(smonData_dateString[smonIdx])
                    smonRootDecimalStat.push_back(str(smonData_decimalStatus[smonIdx]))
                    smonRootBinStat.push_back(smonData_binStatus[smonIdx])
                    smonRootMeaningStat.push_back(smonData_meaningString[smonIdx])

                StatusTree.Fill()
                StatusTree.Write()

            rangeImon = maxValImonMultig - minValImonMultig
            rangeVmon = maxValVmonMultig - minValVmonMultig
            rangeSmon = maxValSmonMultig - minValSmonMultig
            rangeTemp = maxValTempMultig - minValTempMultig
            minValImonMultig = minValImonMultig - 0.05 * rangeImon
            minValVmonMultig = minValVmonMultig - 0.05 * rangeVmon
            minValSmonMultig = minValSmonMultig - 0.05 * rangeSmon
            minValTempMultig = minValTempMultig - 0.05 * rangeTemp
            maxValImonMultig = maxValImonMultig + 0.05 * rangeImon
            maxValVmonMultig = maxValVmonMultig + 0.05 * rangeVmon
            maxValSmonMultig = maxValSmonMultig + 0.05 * rangeSmon
            maxValTempMultig = maxValTempMultig + 0.05 * rangeTemp
            print((
             'chamber: ', chamberList[chIdx]))
            fontSize = 0.018
            Imontmultig1.GetXaxis().SetRangeUser(minDateImonMultig, maxDateImonMultig)
            Imontmultig1.GetYaxis().SetRangeUser(minValImonMultig - 0.5 * rangeImon, maxValImonMultig)
            Imontmultig1.GetYaxis().SetTitle('Monitored current (#muA)')
            Imontmultig1.GetXaxis().SetTimeDisplay(1)
            Imontmultig1.GetXaxis().SetTimeFormat('#splitline{%y-%m-%d}{%H:%M:%S}%F1970-01-01 00:00:00')
            Imontmultig1.GetXaxis().SetLabelOffset(0.025)
            Imontmultig1.GetXaxis().SetLabelSize(fontSize)
            Imontmultig1.GetYaxis().SetLabelSize(fontSize)
            Vmontmultig1.GetXaxis().SetRangeUser(minDateVmonMultig, maxDateVmonMultig)
            Vmontmultig1.GetYaxis().SetRangeUser(minValVmonMultig, maxValVmonMultig + 0.6 * rangeVmon)
            Vmontmultig1.GetYaxis().SetTitle('Monitored voltage (V)')
            Vmontmultig1.GetXaxis().SetTimeDisplay(1)
            Vmontmultig1.GetXaxis().SetTimeFormat('#splitline{%y-%m-%d}{%H:%M:%S}%F1970-01-01 00:00:00')
            Vmontmultig1.GetXaxis().SetLabelOffset(0.025)
            Vmontmultig1.GetXaxis().SetLabelSize(fontSize)
            Vmontmultig1.GetYaxis().SetLabelSize(fontSize)
            Smontmultig1.GetXaxis().SetRangeUser(minDateSmonMultig, maxDateSmonMultig)
            Smontmultig1.GetYaxis().SetRangeUser(minValSmonMultig, maxValSmonMultig)
            Smontmultig1.GetXaxis().SetTimeDisplay(1)
            Smontmultig1.GetXaxis().SetTimeFormat('#splitline{%y-%m-%d}{%H:%M:%S}%F1970-01-01 00:00:00')
            Smontmultig1.GetXaxis().SetLabelOffset(0.025)
            Smontmultig1.GetXaxis().SetLabelSize(fontSize)
            Smontmultig1.GetYaxis().SetLabelSize(fontSize)
            Isontmultig1.GetXaxis().SetRangeUser(minDateIsonMultig, maxDateIsonMultig)
            Isontmultig1.GetYaxis().SetRangeUser(0.05, 1.5)
            Isontmultig1.GetXaxis().SetTimeDisplay(1)
            Isontmultig1.GetXaxis().SetTimeFormat('#splitline{%y-%m-%d}{%H:%M:%S}%F1970-01-01 00:00:00')
            Isontmultig1.GetXaxis().SetLabelOffset(0.025)
            Isontmultig1.GetXaxis().SetLabelSize(fontSize)
            Isontmultig1.GetYaxis().SetLabelSize(fontSize)
            Temptmultig1.GetXaxis().SetRangeUser(minDateTempMultig, maxDateTempMultig)
            Temptmultig1.GetXaxis().SetTimeDisplay(1)
            Temptmultig1.GetXaxis().SetTimeFormat('#splitline{%y-%m-%d}{%H:%M:%S}%F1970-01-01 00:00:00')
            Temptmultig1.GetXaxis().SetLabelOffset(0.025)
            Temptmultig1.GetXaxis().SetLabelSize(fontSize)
            Temptmultig1.GetYaxis().SetLabelSize(fontSize)
            Imontmultig1.Write()
            Vmontmultig1.Write()
            Smontmultig1.Write()
            Isontmultig1.Write()
            Temptmultig1.Write()
            canW = 800
            canH = 800
            canH_ref = 800
            canW_ref = 800
            TopMar = 0.12 * canH_ref
            BotMar = 0.17 * canH_ref
            LeftMar = 0.15 * canW_ref
            RightMar = 0.12 * canW_ref
            cmsPrel = ROOT.TPaveText(0.13, 0.88, 0.355, 0.96, 'brNDC')
            cmsPrel.AddText('CMS Preliminary')
            cmsPrel.SetTextAlign(12)
            cmsPrel.SetShadowColor(transWhite)
            cmsPrel.SetFillColor(transWhite)
            cmsPrel.SetLineColor(transWhite)
            cmsPrel.SetLineColor(transWhite)
            xAxisLab = ROOT.TPaveText(0.6, 0.88, 0.9, 0.92, 'brNDC')
            xAxisLab.AddText('Date(YY-MM-DD) / Time(hh:mm:ss)')
            xAxisLab.SetTextAlign(12)
            xAxisLab.SetShadowColor(transWhite)
            xAxisLab.SetFillColor(transWhite)
            xAxisLab.SetLineColor(transWhite)
            xAxisLab.SetLineColor(transWhite)
            imonCanvas = ROOT.TCanvas('ImonCanvasAllChannels', chamberList[chIdx], 50, 50, 800, 800)
            imonCanvas.SetLeftMargin(LeftMar / canW)
            imonCanvas.SetRightMargin(RightMar / canW)
            imonCanvas.SetTopMargin(TopMar / canH)
            imonCanvas.SetBottomMargin(BotMar / canH)
            Imontmultig1.Draw('AP')
            legendMultiImon.Draw('SAME')
            cmsPrel.Draw('NB')
            xAxisLab.Draw('NB')
            imonCanvas.Write()
            vmonCanvas = ROOT.TCanvas('VmonCanvasAllChannels', chamberList[chIdx], 50, 50, 800, 800)
            vmonCanvas.SetLeftMargin(LeftMar / canW)
            vmonCanvas.SetRightMargin(RightMar / canW)
            vmonCanvas.SetTopMargin(TopMar / canH)
            vmonCanvas.SetBottomMargin(BotMar / canH)
            Vmontmultig1.Draw('AP')
            legendMultiVmon.Draw('SAME')
            cmsPrel.Draw('NB')
            xAxisLab.Draw('NB')
            vmonCanvas.Write()
            smonCanvas = ROOT.TCanvas('SmonCanvasAllChannels', chamberList[chIdx], 50, 50, 800, 800)
            smonCanvas.SetLeftMargin(LeftMar / canW)
            smonCanvas.SetRightMargin(RightMar / canW)
            smonCanvas.SetTopMargin(TopMar / canH)
            smonCanvas.SetBottomMargin(BotMar / canH)
            Smontmultig1.Draw('AP')
            legendMultiImon.Draw('SAME')
            cmsPrel.Draw('NB')
            xAxisLab.Draw('NB')
            smonCanvas.Write()
            chamberNameNoSlash = chamberList[chIdx].replace('/', '_')
            if args.save:
                imonCanvas.SaveAs(dirStringSave + '/Imon_' + chamberNameNoSlash + '_AllElectrodes.png')
            if args.save:
                vmonCanvas.SaveAs(dirStringSave + '/Vmon_' + chamberNameNoSlash + '_AllElectrodes.png')
            del Imontmultig1
            del Vmontmultig1
            del Smontmultig1
            del imonCanvas
            del vmonCanvas
            del smonCanvas

        f1.Close()
        print('\n-------------------------Output--------------------------------')
        print(fileName + ' has been created.')
        verboseprint('It is organised in directories: to change directory use DIRNAME->cd()')
        verboseprint('To draw a TH1 or a TGraph: OBJNAME->Draw()')
        verboseprint('To scan the TTree use for example:\nHV_StatusTree2_2_Top_G3Bot->Scan("","","colsize=26")')
        print('ALL MONITOR TIMES ARE IN UTC, DCS TIMES ARE IN CET')
        return


if __name__ == '__main__':
    main()
# okay decompiling GEMDCSP5Monitor.pyc
