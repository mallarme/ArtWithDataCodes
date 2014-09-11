#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  nflStats.py
#  
#  Copyright 2014 Leandro <Leandro@leandrowar>
#  

from bs4 import BeautifulSoup
import urllib2
from urlparse import urljoin

          
category = ['PASSING','RUSHING','RECEIVING','KICKING','FIELD_GOALS','KICK_RETURNS',
			'PUNTING','SACKS','SCORING','TOUCHDOWNS','TACKLES','INTERCEPTIONS','PLAYER_TOTAL_YARDS']

filename = 'nflStatsWeek1.txt'
file = open(filename,'w')
	
for cat in category:	  
	nflLink = 'http://www.nfl.com/stats/categorystats?archive=false&conference=null&statisticCategory='+cat+'&season=2014&seasonType=REG&experience=&tabSeq=0&qualified=false&Submit=Go'
	
	
	c=urllib2.urlopen(nflLink)
	soup=c.read( )
	soup = BeautifulSoup(soup)
		
	
	table = soup.find('table') 
	rows = table.findAll('tr')[1:]
	print '-'*50
	print cat
	print '-'*50
	file.write(cat+'\n')
	for tr in rows:
		cols = tr.findAll('td')
		for i in range(0,len(cols)):
			a = cols[i].text.replace('	','').replace('\n','') + '|'
			print a,

			file.write(a)
		print '\n'
		file.write('\n')
		
		

file.close()
	
