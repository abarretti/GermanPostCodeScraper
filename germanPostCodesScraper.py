#!/usr/bin/env python
#-*- coding: utf-8 -*-

import urllib

postCodesGermanyURL='https://en.wikipedia.org/wiki/List_of_postal_codes_in_Germany'
urlList = []
cityLine= 0

handlePostCodes = urllib.urlopen(postCodesGermanyURL)
for line in handlePostCodes:
    line = line.rstrip()
    urlStart= line.find('href="/wiki/')
    if line.startswith('<h3><span id="01000–01999"></span><span class="mw-headline"'):
        cityLine=1
    if line.startswith('<h2><span class="mw-headline" id="Old_postal_codes">'):
        cityLine=0            
    if urlStart != -1 and cityLine==1:
        end= line.find('"',urlStart+10)
        city= line[urlStart+12:end]
        urlList.append('https://en.wikipedia.org/wiki/'+city)

for url in urlList:
    cityPage = urllib.urlopen(url)
    for line in cityPage:
        try:
            populationTableCount=populationTableCount+1
        except:
            pass
        if line.startswith('<title>'):
            cityEnd=line.find(' ')
            city= line[7:cityEnd]
        if line.startswith('<th colspan="2" style="text-align:center;text-align:left">Population'):
            populationTableCount=0
        try:
            if populationTableCount==4:
                populationEnd= line.find('</td>')
                population = line[4:populationEnd]
        except:
            pass
    print city, url, population

"""
cd Desktop/PYTHON/MyPythonCode/GermanZipCodes
python ./germanZipCodes.py
"""