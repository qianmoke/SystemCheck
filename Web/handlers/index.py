#-*-coding: utf-8 -*-

from tornado import web
from _collections import defaultdict
import re
from DataMiner.config import pathDict,period

import os
from random import randint
class IndexHandler(web.RequestHandler):
    def get(self):
        lparInfo = []
        regionInfo = []
        for root,dirs,files in os.walk(pathDict['imagePath']):
            for directory in dirs:
                lpar = directory.split('.')[0].split('_')[0]
                region = directory.split('.')[0].split('_')[1]
                lparInfo.append(lpar)
                regionInfo.append(region)
        self.render("report.html",lparInfo = lparInfo,regionInfo = regionInfo,pathDict = pathDict,period=period)

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

class TclassModule(web.UIModule):
    def render(self, lparInfo, regionInfo, pathDict):
        i = randint(0, len(lparInfo)-1)
        imageFile=''
        tclassFile = open(pathDict['templatePath']+'\\tclass.html','w')
        for root, dirs, files in os.walk(pathDict['imagePath'] + '\\'+lparInfo[i] + '_'+regionInfo[i]+'.xlsx.files'):
            for j in xrange(2,len(files),1):
                imageFile = lparInfo[i] + '_'+regionInfo[i]+'.xlsx.files/'+files[j]
                image="<p class=MsoNormal style='margin-left:21.0pt;line-height:150%;text-autospace:\nnone'>\
                        <span lang=EN-US><img width=553 height=349\n\
                        src={{static_url('images/" + imageFile + "')}}></span></p>\n"
                tclassFile.write(image)
        tclassFile.close()
        return self.render_string('tclass.html')