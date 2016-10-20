'''
Created on Dec 21, 2015

@author: joy
'''
import os
from config import dateEnd, dateStart, month
from config import moniPath,tpsPath

def handle(text, outputFile):
    words = text.split("==")
    #print words
    if(words[0].strip()=="STATBUILDLEVEL2.8.2"):
        for line in text.splitlines():
            montime = line.split(" Current time: ")
            if(montime[0] == "=="):
                timetag = montime[-1].strip()
            linetmp = ",".join(line.split()) 
            #print line        
            if(len(linetmp.split(","))>=2 and len(linetmp.split(",")[1].split("]"))>=2 and linetmp.split(",")[1].split("]")[1]== "TransStatINFO1"):
                linetmp2=linetmp.split(",")
                trancount=linetmp2[3]
                if(int(trancount)<0):
                    trancount=0
                tps=linetmp2[4]
                if(float(tps)<0):
                    tps=0.0
                timeTest = timetag.split("/")[2].split()[0]
                timeMonth = timetag.split("/")[1]    
                if ( dateStart <= int(timeTest) <= dateEnd and timeMonth == month):
                    print  timetag + "," + str(trancount) + "," + str(tps)
                    rptFile = open(outputFile+".tps.csv","a")
                    rptFile.write(timetag + "," + str(trancount) + "," + str(tps))
                    rptFile.write("\n")
                    rptFile.close() 
    elif(words[0].strip()=="STATBUILDLEVEL2.7.2" or words[0].strip()=="STATBUILDLEVEL2.7.3"  or words[0].strip()=="STATBUILDLEVEL2.7.8.1" or words[0].strip()=="STATBUILDLEVEL2.7.8" or words[0].strip()=="STATBUILDLEVEL2.7.0"):        
        for line in text.splitlines():
            montime = line.split(" Current time: ")
            if(montime[0] == "=="):
                timetag = montime[-1].strip()
            linetmp = ",".join(line.split())         
            if(len(linetmp.split(","))>=2 and len(linetmp.split(",")[1].split("]"))>=2 and linetmp.split(",")[1].split("]")[1]== "TransStatINFO1"):
                linetmp2=linetmp.split(",")
                trancount=linetmp2[3]
                if(int(trancount)<0):
                    trancount=0
                tps=linetmp2[4]
                if(float(tps)<0):
                    tps=0.0
                timeTest = timetag.split("/")[2].split()[0]
                timeMonth = timetag.split("/")[1]
                if ( dateStart <= int(timeTest) <= dateEnd and timeMonth == month):
                    print  timetag + "," + str(trancount) + "," + str(tps)
                    rptFile = open(outputFile+".tps.csv","a")
                    rptFile.write(timetag + "," + str(trancount) + "," + str(tps))
                    rptFile.write("\n")
                    rptFile.close() 
    elif(words[0].strip()=="STATBUILDLEVEL2.6.6"):        
        for line in text.splitlines():
            montime = line.split(" Current time: ")
            if(montime[0] == "=="):
                timetag = montime[-1].strip()
            linetmp = ",".join(line.split())
            if(linetmp.split(",")[0] == "TaskStatINFO1"):
                linetmp2=linetmp.split(",")
                trancount=linetmp2[2]
                if(long(trancount)<0):
                    trancount=0
                tps=linetmp2[3]
                if(long(tps)<0):
                    trancount=0
                timeTest = timetag.split("/")[2].split()[0]
                timeMonth = timetag.split("/")[1]
                if ( dateStart <= int(timeTest) <= dateEnd and timeMonth == month):
                    print  timetag + "," + str(trancount) + "," + str(tps)
                    rptFile = open(outputFile+".tps.csv","a")
                    rptFile.write(timetag + "," + str(trancount) + "," + str(tps))
                    rptFile.write("\n")
                    rptFile.close() 
    elif(words[0].strip()=="STATBUILDLEVEL2.4.3" or words[0].strip()=="STATBUILDLEVEL2.1.5" or words[0].strip()=="STATBUILDLEVEL2.3.4"):       
        for line in text.splitlines():
            montime = line.split(" Current time: ")
            if(montime[0] == "=="):
                timetag = montime[-1].strip()
            linetmp = ",".join(line.split())
            if(linetmp.split(",")[0] == "TaskStatINFO1"):
                linetmp2=linetmp.split(",")
                trancount=linetmp2[1]
                if(long(trancount)<0):
                    trancount=0
                trancount_f=float(trancount)
                tps_f=float('%0.2f'%trancount_f)/120
                tps=float('%0.2f'%tps_f)
                timeTest = timetag.split("/")[2].split()[0]
                timeMonth = timetag.split("/")[1]
                if ( dateStart <= int(timeTest) <= dateEnd and timeMonth == month ):
                    print  timetag + "," + str(trancount) + "," + str(tps)
                    rptFile = open(outputFile+".tps.csv","a")
                    rptFile.write(timetag + "," + str(trancount) + "," + str(tps))
                    rptFile.write("\n")
                    rptFile.close() 
               
def readFile(moniPath, tpsPath, moniFile, outputFile): 
    #try:
        rptFile = open(moniPath  + "/" + moniFile ,"r")
        text = rptFile.read()
        words = text.split("====================================")
        for element in words:
            #print element
            handle(element,tpsPath + "/" +outputFile)
    #except:
    #    rptFile.close()     
