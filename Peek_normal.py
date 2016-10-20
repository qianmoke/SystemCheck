'''
Created on Dec 21, 2015

@author: joy
'''
import os
from config import dateEnd, dateStart, month
from config import moniPath,peekPath
from collections import OrderedDict
from re import search

def handle(text,fileName):
    peekDict = OrderedDict()
    timetag = ""
    for line in text.splitlines():
        if (search("TClass", line) and ( not search("TClassINFO00",line))):
                peekDict[line.split()[0]] = list()
                peekDict[line.split()[0]].append(line.split()[4])            
        else:
            montime = line.split(" Current time: ")
            if(montime[0] == "=="):
                timetag = montime[-1].strip()
    timeTest = timetag.split("/")[2].split()[0]
    timeMonth = timetag.split("/")[1]    
    if ( dateStart <= int(timeTest) <= dateEnd and timeMonth == month):
        data = timetag
        for key in peekDict.keys():
            data += "," + str(peekDict[key][0])
        print data
        try:
            rptFile = open(fileName + ".peek.csv","a")
            rptFile.write(data)
            rptFile.write("\n")
        except Exception:
            print Exception.message
        finally:    
            rptFile.close() 
                 
def readFile(moniPath, peekPath, moniFile,outputFile): 
    #try:
        rptFile = open(moniPath + "/" + moniFile ,"r")
        text = rptFile.read()
        words = text.split("====================================")
        for element in words:
            if element != "\n":
                handle(element,peekPath + "/" + outputFile)
        rptFile.close()
    #except:
    #    rptFile.close()     

if __name__ == "__main__":
    for root, dirs, files in os.walk(moniPath):
        for moniFile in files:
            print moniFile
            readFile(moniPath, peekPath, moniFile)