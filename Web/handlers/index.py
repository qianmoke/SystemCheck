#-*-coding: utf-8 -*-

from tornado import web
from _collections import defaultdict
import re
from DataMiner.config import pathDict,period

import os
from random import randint
class IndexHandler(web.RequestHandler):
    def get(self):
        systemInfo = []
        for root,dirs,files in os.walk(pathDict['imagePath']):
            for directory in dirs:
                lpar = directory.split('.')[0].split('_')[0]
                if re.search('pipsv',directory) or re.search('phbps',directory) or re.search('prcps', directory):
                    system=lpar[:5]
                elif re.search('pccmcis',directory) or re.search('mcisnet',directory):
                    system=lpar[:7]
                else:
                    system=lpar[:4]
                if system not in systemInfo:
                    systemInfo.append(system)
        self.render("index2.html",systemInfo=systemInfo)

class CicsHandler(web.RequestHandler):
    def get(self):
        lparInfo = []
        regionInfo = []
        sysName=self.get_argument("system", "IPSV", True)
        for root,dirs,files in os.walk(pathDict['imagePath']):
            for directory in dirs:
                if (sysName == 'pips'):
                    if ((not re.search('pipsv',directory)) and re.search(sysName,directory)):
                        lpar = directory.split('.')[0].split('_')[0]
                        region = directory.split('.')[0].split('_')[1]
                        lparInfo.append(lpar)
                        regionInfo.append(region)
                else:
                    if re.search(sysName,directory):
                        lpar = directory.split('.')[0].split('_')[0]
                        region = directory.split('.')[0].split('_')[1]
                        lparInfo.append(lpar)
                        regionInfo.append(region)
        tclass = randint(0, len(lparInfo)-1)
        files=os.listdir(pathDict['imagePath'] + '\\'+lparInfo[tclass] + '_'+regionInfo[tclass]+'.xlsx.files')                
        self.render("report.html",lparInfo = lparInfo,regionInfo = regionInfo,pathDict = pathDict,period=period,tclass=tclass,files=files)

class RegionModule(web.UIModule):
    def render(self, lpar, region, pathDict):
        dataDict=defaultdict(list)
        with open(pathDict['maxPath']+'\\tps.csv') as maxFile:
            for line in maxFile:
                if re.search(lpar+'_'+region,line):
                    if re.search('tps',line):
                        tps=line.split(',')[3]
                        tpsTime=line.split(',')[2]
                    if re.search('peek',line):
                        peek=line.split(',')[3]
                        peekTime=line.split(',')[2]
        dataDict['tps'].append(tps)
        dataDict['tps'].append(tpsTime)
        dataDict['peek'].append(peek)
        dataDict['peek'].append(peekTime)
        return self.render_string('region.html', lpar = lpar, region = region, dataDict = dataDict)
    
class TpsModule(web.UIModule):
    def render(self, lpar, region, pathDict):
        with open(pathDict['maxPath']+'\\tps.csv') as maxFile:
            for line in maxFile:
                if re.search(lpar+'_'+region,line):
                    if re.search('tps',line):
                        tps=line.split(',')[3]
                    if re.search('peek',line):
                        peek=line.split(',')[3]     
        return self.render_string('tps.html', lpar = lpar, region = region, tps = tps, peek=peek)
    
class PoolModule(web.UIModule):
    def render(self, lpar, region, pathDict):
        poolInfo=[0,0,0,0]
        with open(pathDict['maxPath']+'\\pool.csv') as maxFile:
            for line in maxFile:
                if (re.search(lpar,line) and (re.search(region,line))):
                        poolInfo = line.split(',')[1:]     
        return self.render_string('pool.html', lpar = lpar, region = region, poolInfo = poolInfo)