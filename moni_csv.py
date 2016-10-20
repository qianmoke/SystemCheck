'''
Created on Dec 21, 2015

@author: joy
'''

from config import dateEnd, dateStart, month
from collections import OrderedDict
from re import search

def handle(text,peekPath, tpsPath, outputFile):
    peekDict = OrderedDict()
    timetag = ""
    words = text.split("==")
    for line in text.splitlines():
        if (search("TClass", line) and (not search("TClassINFO_DFHTCL00",line) and (not search("TClassINFO00",line)))):
                peekDict[line.split()[0]] = list()
                peekDict[line.split()[0]].append(line.split()[4])
        elif(search("TransStatINFO1",line)):
            trancount,tps=tpsCal(words,line)
        else:
            montime = line.split(" Current time: ")
            if(montime[0] == "=="):
                timetag = montime[-1].strip()
    timeTest = timetag.split("/")[2].split()[0]
    timeMonth = timetag.split("/")[1]    
    if ( dateStart <= int(timeTest) <= dateEnd and timeMonth == month):
        peekData = timetag
        tpsData = timetag + "," + str(trancount) + "," + str(tps)
        for key in peekDict.keys():
            #print key+":"+peekDict[key][0]
            peekData += "," + str(peekDict[key][0])
        print "INFO:peek-" + peekData
        print "INFO:tps-" + tpsData
        try:
            peekFile = open(peekPath + "/" + outputFile + ".peek.csv","a")
            peekFile.write(peekData)
            peekFile.write("\n")
            tpsFile = open(tpsPath + "/" + outputFile + ".tps.csv","a")
            tpsFile.write(tpsData)
            tpsFile.write("\n")
        except Exception:
            print Exception.message
        finally:    
            peekFile.close()
            tpsFile.close() 
                 
def tpsCal(words, line):
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
    return trancount,tps



def readFile(moniPath, peekPath, tpsPath, moniFile,outputFile): 
    try:
        rptFile = open(moniPath + "/" + moniFile ,"r")
        text = rptFile.read()
        words = text.split("====================================")
        for element in words:
            if element != "\n":
                handle(element, peekPath, tpsPath, outputFile)
    finally:
        rptFile.close()
