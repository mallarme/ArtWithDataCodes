#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  dataAnalysis.py
#  
#  Copyright 2014 Leandro <Leandro@leandrowar>
#  
import pandas as pd
import io
import urllib2
import bz2


#Abrindo a URL e descompactando o arquivo .bz2 
url = "https://d396qusza40orc.cloudfront.net/repdata%2Fdata%2FStormData.csv.bz2"
raw_bz2 = urllib2.urlopen(url).read()
data = bz2.decompress(raw_bz2)
df = pd.read_csv(io.BytesIO(data))
df.head()


subSet = df[['BGN_DATE','PROPDMG','CROPDMG','EVTYPE','INJURIES','FATALITIES']]


