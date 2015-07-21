#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import re
import urllib

def getpdfs(inputurl):
    r = requests.get(inputurl)
    localDir = 'G:\\ljppdfs\\'
    urlList = []                                  #存储提供pdf下载的url列表
    for eachline in r:                 
        line = eachline.strip()                   #去除首位空格
        if re.match('.*PDF.*',line):              #匹配含PDF的行
            wordList = line.split('\"')
            for word in wordList:
                if re.match('.*\.pdf$',word):
                    urlList.append(word)
                    
    for everyURL in urlList:
        wordItems = everyURL.split('/')
        for item in wordItems:
            if re.match('.*\.pdf$',item):
                PDFName = item
        localPDF = localDir + PDFName
        try:
            urllib.urlretrieve(everyURL,localPDF)
        except Exception,e:
            continue
            
ljpurl = 'http://ljp.gcess.cn/dct/page/65537'
getpdfs(ljpurl)