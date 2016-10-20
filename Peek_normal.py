'''
Created on Dec 21, 2015

@author: joy
'''
import os
from config import dateEnd, dateStart, month
from config import moniPath,peekPath

def handle(text,fileName):
    #global timetag,BANCS000,CMS00000,DFHTCL01,DFHTCL02,DFHTCL03,DFHTCL04,DFHTCL05,DFHTCL06,DFHTCL07,DFHTCL08,DFHTCL09,DFHTCL10,HDQS0000,RCPS0001,RCPS0002
    #print line
    #print openfile
    for line in text.splitlines():
        montime = line.split(" Current time: ")
        if(montime[0] == "=="):
            timetag = montime[-1].strip()
        linetmp=",".join(line.split())
        if(linetmp.split(",")[0] == "TClassINFO01"):
            linetmp2=linetmp.split(",")
            print linetmp2
            TClassINFO01=linetmp2[4]
        elif(linetmp.split(",")[0] == "TClassINFO02"):
            linetmp2=linetmp.split(",")
            TClassINFO02=linetmp2[4]
        elif(linetmp.split(",")[0] == "TClassINFO03"):
            linetmp2=linetmp.split(",")
            TClassINFO03=linetmp2[4]
        elif(linetmp.split(",")[0] == "TClassINFO04"):
            linetmp2=linetmp.split(",")
            TClassINFO04=linetmp2[4]
        elif(linetmp.split(",")[0] == "TClassINFO05"):
            linetmp2=linetmp.split(",")
            TClassINFO05=linetmp2[4]
        elif(linetmp.split(",")[0] == "TClassINFO06"):
            linetmp2=linetmp.split(",")
            TClassINFO06=linetmp2[4]
        elif(linetmp.split(",")[0] == "TClassINFO07"):
            linetmp2=linetmp.split(",")
            TClassINFO07=linetmp2[4]
        elif(linetmp.split(",")[0] == "TClassINFO08"):
            linetmp2=linetmp.split(",")
            TClassINFO08=linetmp2[4]
        elif(linetmp.split(",")[0] == "TClassINFO09"):
            linetmp2=linetmp.split(",")
            TClassINFO09=linetmp2[4]
        elif(linetmp.split(",")[0] == "TClassINFO10"):
            linetmp2=linetmp.split(",")
            TClassINFO10=linetmp2[4]
            timeTest = timetag.split("/")[2].split()[0]
            timeMonth = timetag.split("/")[1]    
            if ( dateStart <= int(timeTest) <= dateEnd and timeMonth == month):
                print  timetag + ","  + str(TClassINFO01) + "," + str(TClassINFO02) + "," + str(TClassINFO03) + "," + str(TClassINFO04) + "," + str(TClassINFO05) + "," + str(TClassINFO06) + "," + str(TClassINFO07) + "," + str(TClassINFO08) + "," + str(TClassINFO09) + "," + str(TClassINFO10) 
                rptFile = open(fileName + ".peek.csv","a")
                rptFile.write(timetag + "," + str(TClassINFO01) + "," + str(TClassINFO02) + "," + str(TClassINFO03) + "," + str(TClassINFO04) + "," + str(TClassINFO05) + "," + str(TClassINFO06) + "," + str(TClassINFO07) + "," + str(TClassINFO08) + "," + str(TClassINFO09) + "," + str(TClassINFO10))
                rptFile.write("\n")
                rptFile.close() 
                 
def readFile(moniPath, peekPath, moniFile,outputFile): 
    #try:
        rptFile = open(moniPath + "/" + moniFile ,"r")
        text = rptFile.read()
        words = text.split("====================================")
        for element in words:
            handle(element,peekPath + "/" + outputFile)
        rptFile.close()
    #except:
    #    rptFile.close()     

if __name__ == "__main__":
    for root, dirs, files in os.walk(moniPath):
        for moniFile in files:
            print moniFile
            readFile(moniPath, peekPath, moniFile)