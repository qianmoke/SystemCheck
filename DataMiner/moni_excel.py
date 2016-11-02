'''
Created on Dec 21, 2015

@author: joy
'''

from config import period,pathDict
from collections import OrderedDict
from re import search,match
import xlsxwriter
from DataMiner import chart
month = period[0]
dateStart = period[1]
dateEnd = period[2]
def processLine(text, peekDict, tpsDict, maxPoolUse):
    tmpDict=OrderedDict()
    timetag = ""
    tps = (0,0.0)
    regionPool, regionPoolConfig, sharedPool, sharedPoolConfig = (0, 0, 0, 0)
    words = text.split("==")
    for line in text.splitlines():
        if (search("TClass", line) and (not search("TClassINFO_DFHTCL00",line) and (not search("TClassINFO00",line)))):
            tmpDict[line.split()[0]] = line.split()[4]
        elif(search("TransStatINFO1\t",line)):
            tps = calTps(words,line)
        elif(search("RegionPoolINFO",line)):
            regionPool = long(line.split()[4])
            if (maxPoolUse[1] == 0):
                regionPoolConfig = long(line.split()[1])
                maxPoolUse[1] = regionPoolConfig                
        elif(search("SharedPoolINFO",line)):
            sharedPool = long(line.split()[4])
            if (maxPoolUse[3] == 0):
                sharedPoolConfig = long(line.split()[1])
                maxPoolUse[3] = sharedPoolConfig
        else:
            montime = line.split(" Current time: ")
            if(montime[0] == "=="):
                timetag = montime[-1].strip()
    timeTest = timetag.split("/")[2].split()[0]
    timeMonth = timetag.split("/")[1]    
    if ( dateStart <= int(timeTest) <= dateEnd and timeMonth == month):
        peekDict[timetag] = tmpDict
        tpsDict[timetag] = tps
        if regionPool > maxPoolUse[0]:
            maxPoolUse[0] = regionPool
        if sharedPool > maxPoolUse[2]:
            maxPoolUse[2] = sharedPool
        print timetag
        
        
def calTps(words, line):
    if(words[0].strip()=="STATBUILDLEVEL2.6.6"):
        trancount=line.split()[2]
        if(long(trancount)<0):
            trancount=0
        tps=line.split()[3]
        if(long(tps)<0):
            trancount=0
    elif(words[0].strip() in ["STATBUILDLEVEL2.4.3", "STATBUILDLEVEL2.1.5", "STATBUILDLEVEL2.3.4"]):       
                trancount=line.split()[1]
                if(long(trancount)<0):
                    trancount=0
                trancount_f=float(trancount)
                tps_f=float('%0.2f'%trancount_f)/120
                tps=float('%0.2f'%tps_f)
    else:
        trancount=line.split()[3]
        if(int(trancount)<0):
            trancount=0
        tps=line.split()[4]
        if(float(tps)<0):
            tps=0.0
    print line.split()[4]
    return trancount,tps


def processFile(moniFile, peekDict, tpsDict): 
    try:
        maxPoolUse = [0, 0, 0, 0]
        rptFile = open(moniFile ,"r")
        text = rptFile.read()
        words = text.split("====================================")
        for element in words:
            if ((element != "\n") and element != ''):
                processLine(element, peekDict, tpsDict, maxPoolUse)
        if (maxPoolUse[0] != 0):
            for i in xrange(len(maxPoolUse)):
                maxPoolUse[i]=str(maxPoolUse[i])
            poolFile = open(pathDict['maxPath']+'/pool.csv','a')
            poolFile.write(moniFile+',' + ','.join(maxPoolUse)+'\n')
            poolFile.close()
    finally:
        rptFile.close()

def excelProcess(reportPath, peekDict, tpsDict):
    for region in peekDict.keys():
        workbook = xlsxwriter.Workbook(reportPath + "/" + region + '.xlsx')
        regionDict = peekDict[region]
        rowCount = 1
        if workbook.sheetnames.has_key("Tps"):
            tpsSheet = workbook.sheetnames["Tps"]
        else:
            tpsSheet = workbook.add_worksheet('Tps')
        if workbook.sheetnames.has_key("TclassPeekStacked"):
            peekSheet = workbook.sheetnames["TclassPeekStacked"]
        else:
            peekSheet = workbook.add_worksheet('TclassPeekStacked')
        peekSheet.write(0,0,'timeTag')
        tpsSheet.write(0, 0 ,'timeTag')
        tpsSheet.write(0, 1 ,'tranCount')
        tpsSheet.write(0, 2 ,'Tps')
        for timeTag in regionDict.keys():
            timeTagDict = regionDict[timeTag]
            clomCount = 1
            peekSheet.write(rowCount, 0, str(timeTag))
            for tran in timeTagDict.keys():
                tranCount = timeTagDict[tran]
                if workbook.sheetnames.has_key(tran):
                    tmpWorkSheet = workbook.sheetnames[tran]
                else:
                    tmpWorkSheet = workbook.add_worksheet(tran)
                tmpWorkSheet.write(0, 0,'timeTag')
                tmpWorkSheet.write(0, 1, tran)
                tmpWorkSheet.write(rowCount, 0, str(timeTag))
                tmpWorkSheet.write(rowCount, 1, int(tranCount))
                peekSheet.write(0,clomCount,str(tran))
                peekSheet.write(rowCount, clomCount, int(tranCount))
                clomCount +=1
            tpsSheet.write(rowCount, 0, str(timeTag))
            tpsSheet.write(rowCount, 1, int(tpsDict[region][timeTag][0]))
            tpsSheet.write(rowCount, 2, float(tpsDict[region][timeTag][1]))
            rowCount +=1
        tclassnum = 0
        for sheetName in workbook.sheetnames.keys():
            if sheetName == 'Tps':
                chart.tpsChart(workbook, workbook.sheetnames[sheetName], rowCount)
            elif sheetName == 'TclassPeekStacked':
                chart.peekChartAll(workbook, workbook.sheetnames[sheetName], rowCount, clomCount)
            else:
                chart.peekChartOne(sheetName, tclassnum, workbook, workbook.sheetnames[sheetName], rowCount)
                tclassnum +=1
        workbook.close()
    
def maxCal(maxPath, peekDict,tpsDict):
    maxFile = open(maxPath + '/tps.csv','a')
    for region in peekDict.keys():
        tranCount=0
        maxTranCount=0
        maxTps=0
        tpsTime=''
        peekTime=''
        regionDict = peekDict[region]
        for timeTag in regionDict.keys():
            timeTagDict = regionDict[timeTag]
            for tran in timeTagDict.keys():
                tranCount += int(timeTagDict[tran])
            if tranCount > maxTranCount:
                maxTranCount=tranCount
                peekTime=timeTag
            if float(tpsDict[region][timeTag][1]) > maxTps:
                maxTps = float(tpsDict[region][timeTag][1])
                tpsTime=timeTag
            tranCount = 0
        
        tpsData=("%s,tps,%s,%s\n")%(region,tpsTime,maxTps)
        peekData=("%s,peek,%s,%s\n")%(region,peekTime,maxTranCount)
        maxFile.write(tpsData)
        maxFile.write(peekData)        
    maxFile.close()
