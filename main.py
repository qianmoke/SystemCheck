from collections import OrderedDict,defaultdict
from DataMiner.config import pathDict
from DataMiner.moni_excel import processFile,excelProcess,maxCal
from DataMiner.exceltoimage import exceltoimage,imagechoose
import os,re
from Web.server import  main
import multiprocessing
from time import sleep

def processThread(fileDict, outputFile):
    peekDict = defaultdict(OrderedDict)
    tpsDict = defaultdict(OrderedDict)
    for moniFile in fileDict[outputFile]:
        processFile(pathDict['moniPath'] + '/' +moniFile, peekDict[outputFile],tpsDict[outputFile])
    excelProcess(pathDict['reportPath'], peekDict, tpsDict)
    maxCal(pathDict['maxPath'], peekDict, tpsDict)
    
def schedule(processDict):
    alive = 0
    for name in processDict.keys():
        if processDict[name][0].is_alive():
            alive += 1
            
    for name in processDict.keys():
        if alive < 4 and processDict[name][1] == 0:
            processDict[name][0].start()
            processDict[name][1]=1
            alive += 1  
      
    if alive == 0:
        for xlsfile in os.listdir(pathDict['reportPath']):
            print xlsfile
            exceltoimage(pathDict['reportPath'], xlsfile, pathDict['imagePath'])    
            for root,dirs,files in os.walk(pathDict['imagePath']):
                for directory in dirs:
                    for fileName in os.listdir(pathDict['imagePath']+"\\"+directory):
                        imagechoose(pathDict['imagePath']+"\\"+directory, fileName)
        main()

if __name__ == "__main__":
    fileDict = defaultdict(list)

    processDict = defaultdict(list)  
    for moniFile in os.listdir(pathDict['moniPath']):
        if re.search("_", moniFile):
            outputFile = "_".join(moniFile.split("_")[0:2])
        else:
            outputFile = "_".join(moniFile.split(".")[1:3])
        fileDict[outputFile].append(moniFile)
    for outputFile in fileDict.keys():
        #excelProcess(pathDict['reportPath'], peekDict, tpsDict) 
        process=multiprocessing.Process(target = processThread, args=(fileDict, outputFile,))
        processDict[process.name] += [process, 0]
    while True:
        schedule(processDict)
        sleep(1)
    main()