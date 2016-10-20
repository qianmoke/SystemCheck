import Tps_normal
import report_peek_normal
import report_tps
import Peek_normal
import report_peek_mcis
import os,re
from config import moniPath,tpsPath,reportPath,peekPath,imagePath
from exceltoimage import exceltoimage,imagechoose

if __name__ == "__main__":
    for root, dirs, files in os.walk(moniPath):
        for moniFile in files:
            if re.search("-", moniFile):
                outputFile = "-".join(moniFile.split("-")[0:2])
            else:
                outputFile = "-".join(moniFile.split(".")[1:3])
            Tps_normal.readFile(moniPath, tpsPath, moniFile, outputFile)
            Peek_normal.readFile(moniPath, peekPath, moniFile, outputFile)
    for root, dirs, files in os.walk(tpsPath):
        for tpsFile in files:
            print tpsFile
            tpstablelist = report_tps.readtps(tpsPath + "\\" + tpsFile)
            report_tps.tps_line(tpstablelist,reportPath + "\\" + tpsFile)
    
    for root, dirs, files in os.walk(peekPath):
        for peekFile in files:
            print peekFile
            #peektablelist = report_peek_normal.readpeek(peekPath + "/" + peekFile)
            #report_peek_normal.TClassPeek_area_stacked(peektablelist, reportPath + "/" + peekFile)
            peektablelist = report_peek_mcis.readpeek(peekPath + "\\" + peekFile)
            #print peektablelist
            report_peek_normal.TClassPeek_area_stacked(peektablelist, reportPath + "\\" + peekFile)
    for root,dirs,files in os.walk(reportPath):
        for xlsfile in files:
            print xlsfile
            exceltoimage(reportPath, xlsfile, imagePath)
    for root,dirs,files in os.walk(imagePath):
        for directory in dirs:
            for root,dirs,files in os.walk(imagePath+"\\"+directory):
                for fileName in files:
                    imagechoose(imagePath+"\\"+directory, fileName)