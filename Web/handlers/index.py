#-*-coding: utf-8 -*-

from tornado import web
from _collections import defaultdict
import re
from DataMiner.config import pathDict,period
imagePath = pathDict['imagePath']
from os import walk
class IndexHandler(web.RequestHandler):
    def get(self):
        lparInfo = []
        regionInfo = []
        for root,dirs,files in walk(imagePath):
            for directory in dirs:
                lpar = directory.split('.')[0].split('_')[0]
                region = directory.split('.')[0].split('_')[1]
                lparInfo.append(lpar)
                regionInfo.append(region)
        self.render("report.html",lparInfo = lparInfo,regionInfo = regionInfo,imagePath = imagePath,period=period)

class RegionModule(web.UIModule):
    def render(self, lpar, region, imagePath, maxPath):
        dataDict=defaultdict(list)
        with open(maxPath+'\\tps.csv') as maxFile:
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
        return self.render_string('region.html', lpar = lpar, region = region, imagePath = imagePath, dataDict = dataDict)
    
class TpsModule(web.UIModule):
    def render(self, lpar, region, maxPath):
        with open(maxPath+'\\tps.csv') as maxFile:
            for line in maxFile:
                if re.search(lpar+'_'+region,line):
                    if re.search('tps',line):
                        tps=line.split(',')[3]
                    if re.search('peek',line):
                        peek=line.split(',')[3]     
        return self.render_string('tps.html', lpar = lpar, region = region, tps = tps, peek=peek)
    
class PoolModule(web.UIModule):
    def render(self, lpar, region, poolPath):
        with open(poolPath+'\\pool.csv') as maxFile:
            for line in maxFile:
                if re.search(lpar+'_'+region,line):
                        regionPool=line.split(',')[1]
                        shardPool=line.split(',')[2]     
        return self.render_string('pool.html', lpar = lpar, region = region, regionPool = regionPool, shardPool = shardPool)

class TclassModule(web.UIModule):
    def render(self, lpar, region, imagePath):

        return self.render_string('pool.html', lpar = lpar, region = region, regionPool = regionPool, shardPool = shardPool)