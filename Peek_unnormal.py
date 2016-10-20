'''
Created on Dec 21, 2015

@author: joy
'''
import os
import re
from config import dateEnd, dateStart, month
from config import moniPath,peekPath

def handle(text,fileName):
    #global timetag,BANCS000,CMS00000,DFHTCL01,DFHTCL02,DFHTCL03,DFHTCL04,DFHTCL05,DFHTCL06,DFHTCL07,DFHTCL08,DFHTCL09,DFHTCL10,HDQS0000,RCPS0001,RCPS0002
    #print line
    #print openfile
    if re.search(".bak", fileName):
        fileName = fileName[:-4]
    for line in text.splitlines():
        montime = line.split(" Current time: ")
        if(montime[0] == "=="):
            timetag = montime[-1].strip()
            #print timetag
        #print linetmp
        '''if(linetmp.split(",")[0] == "RegionPoolINFO"):
            for tmp in linetmp.split(","):
                #print  "****" +str(tmp) + "***"
                print "" 
                '''
        linetmp=",".join(line.split())
        #print linetmp
        if(linetmp.split(",")[0] == "TClassINFO_BANCS000"):
            linetmp2=linetmp.split(",")
            BANCS000=linetmp2[4]
        elif(linetmp.split(",")[0] == "TClassINFO_CMS00000"):
            linetmp2=linetmp.split(",")
            CMS00000=linetmp2[4]
        elif(linetmp.split(",")[0] == "TClassINFO_DFHTCL01"):
            linetmp2=linetmp.split(",")
            DFHTCL01=linetmp2[4]
        elif(linetmp.split(",")[0] == "TClassINFO_DFHTCL02"):
            linetmp2=linetmp.split(",")
            DFHTCL02=linetmp2[4]
        elif(linetmp.split(",")[0] == "TClassINFO_DFHTCL03"):
            linetmp2=linetmp.split(",")
            DFHTCL03=linetmp2[4]
        elif(linetmp.split(",")[0] == "TClassINFO_DFHTCL04"):
            linetmp2=linetmp.split(",")
            DFHTCL04=linetmp2[4]
            timeTest = timetag.split("/")[2].split()[0]
            timeMonth = timetag.split("/")[1]    
            '''if ( dateStart <= int(timeTest) <= dateEnd and timeMonth == month):
                  print  timetag + ","  + str(TClassINFO01) + "," + str(TClassINFO02) + "," + str(TClassINFO03) + "," + str(TClassINFO04) + "," + str(TClassINFO05) + "," + str(TClassINFO06) 
                  rptFile = open(file + ".peek.csv","a")
                  rptFile.write(timetag + "," + str(TClassINFO01) + "," + str(TClassINFO02) + "," + str(TClassINFO03) + "," + str(TClassINFO04) + "," + str(TClassINFO05) + "," + str(TClassINFO06))
                  rptFile.write("\n")
                  rptFile.close()'''
        elif(linetmp.split(",")[0] == "TClassINFO_DFHTCL05"):
            linetmp2=linetmp.split(",")
            DFHTCL05=linetmp2[4]
        elif(linetmp.split(",")[0] == "TClassINFO_DFHTCL06"):
            linetmp2=linetmp.split(",")
            DFHTCL06=linetmp2[4]
        elif(linetmp.split(",")[0] == "TClassINFO_DFHTCL07"):
            linetmp2=linetmp.split(",")
            DFHTCL07=linetmp2[4]
        elif(linetmp.split(",")[0] == "TClassINFO_DFHTCL08"):
            linetmp2=linetmp.split(",")
            DFHTCL08=linetmp2[4]
        elif(linetmp.split(",")[0] == "TClassINFO_DFHTCL09"):
            linetmp2=linetmp.split(",")
            DFHTCL09=linetmp2[4]
        elif(linetmp.split(",")[0] == "TClassINFO_DFHTCL10"):
            linetmp2=linetmp.split(",")
            DFHTCL10=linetmp2[4]
        elif(linetmp.split(",")[0] == "TClassINFO_HDQS0000"):
            linetmp2=linetmp.split(",")
            HDQS0000=linetmp2[4]
        elif(linetmp.split(",")[0] == "TClassINFO_RCPS0001"):
            linetmp2=linetmp.split(",")
            RCPS0001=linetmp2[4]
        elif(linetmp.split(",")[0] == "TClassINFO_RCPS0002"):
            linetmp2=linetmp.split(",")
            RCPS0002=linetmp2[4]
            timeTest = timetag.split("/")[2].split()[0]
            timeMonth = timetag.split("/")[1]    
            if ( dateStart <= int(timeTest) <= dateEnd and timeMonth == month):
                print  timetag + "," + str(BANCS000) + "," + str(CMS00000) + "," + str(DFHTCL01) + "," + str(DFHTCL02) + "," + str(DFHTCL03) + "," + str(DFHTCL04) + "," + str(DFHTCL05) + "," + str(DFHTCL06) + "," + str(DFHTCL07) + "," + str(DFHTCL08) + "," + str(DFHTCL09) + "," + str(DFHTCL10) + "," + str(HDQS0000) + "," + str(RCPS0001) + "," + str(RCPS0002)
                rptFile = open(fileName +".peek.csv","a")
                rptFile.write(timetag + "," + str(BANCS000) + "," + str(CMS00000) + "," + str(DFHTCL01) + "," + str(DFHTCL02) + "," + str(DFHTCL03) + "," + str(DFHTCL04) + "," + str(DFHTCL05) + "," + str(DFHTCL06) + "," + str(DFHTCL07) + "," + str(DFHTCL08) + "," + str(DFHTCL09) + "," + str(DFHTCL10) + "," + str(HDQS0000) + "," + str(RCPS0001) + "," + str(RCPS0002))
                rptFile.write("\n")
                rptFile.close()
                 
def readFile(moniPath, peekPath, moniFile): 
    #try:
        rptFile = open(moniPath + "/" + moniFile ,"r")
        text = rptFile.read()
        words = text.split("====================================")
        for element in words:
            handle(element,peekPath + "/" + moniFile)
        rptFile.close()
    #except:
    #    rptFile.close()     

if __name__ == "__main__":
    for root, dirs, files in os.walk(moniPath):
        for moniFile in files:
            print moniFile
            readFile(moniPath, peekPath, moniFile)