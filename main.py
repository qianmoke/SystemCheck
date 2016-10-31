from collections import OrderedDict,defaultdict
from DataMiner.config import pathDict
from DataMiner.moni_excel import processFile,excelProcess,maxCal
from DataMiner.exceltoimage import exceltoimage,imagechoose
import os,re
from Web.server import  main

if __name__ == "__main__":
    peekDict = defaultdict(OrderedDict)
    tpsDict = defaultdict(OrderedDict)  
    for root, dirs, files in os.walk(pathDict['moniPath']):
        for moniFile in files:
            if re.search("_", moniFile):
                outputFile = "_".join(moniFile.split("_")[0:2])
            else:
                outputFile = "_".join(moniFile.split(".")[1:3])
            processFile(pathDict['moniPath'] + '/' +moniFile, peekDict[outputFile],tpsDict[outputFile])
    excelProcess(pathDict['reportPath'], peekDict, tpsDict)
    maxCal(pathDict['maxPath'], peekDict, tpsDict)
    
    for root,dirs,files in os.walk(pathDict['reportPath']):
        for xlsfile in files:
            print xlsfile
            exceltoimage(pathDict['reportPath'], xlsfile, pathDict['imagePath'])
    
    for root,dirs,files in os.walk(pathDict['imagePath']):
        for directory in dirs:
            for root,dirs,files in os.walk(pathDict['imagePath']+"\\"+directory):
                for fileName in files:
                    imagechoose(pathDict['imagePath']+"\\"+directory, fileName)
    main()