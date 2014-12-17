#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  feedReader.py
#  
#  Copyright 2013 Leandro Guerra <leandro@leandrowar>

import feedparser
from bs4 import BeautifulSoup
import urllib2
from urlparse import urljoin
import unicodedata	
import sys
import pymongo
import datetime
import time
from alertaEmail import alertaEmail
from GChartWrapper import *
import numpy

# --- FUNCAO PARA CHECAR A CONEXAO COM A INTERNET --- #
def internetOn():
	try:
		response = urllib2.urlopen('http://74.125.113.99',timeout=1)
		return 1
	except: 
		pass
		return 0
# --- FIM DA FUNCAO PARA CHECAR A CONEXAO COM A INTERNET --- #

# --- BLOCO DE CODIGO PARA ARMAZENAR AS HEADLINES ---#
def writeHeadlines (headline,data,linkF):
	
	# Conectando com o Mongo
	connection = pymongo.Connection("mongodb://localhost", safe=True)

	# handles para a base de dados
	db = connection.fia
	feeds = db.feeds
	
	query = {'headline':headline,'link':linkF}
	
	doc = None
	try:
		doc = feeds.find_one(query)     #Se o headline ja existir na base
									  #altera o valor de doc para não haver novo insert
	except:
		print '--- ERRO NO findOne() ---', sys.exc_info()[0]
	
	if (doc == None):
		doc = {'headline':headline, 'data':data, 'link':linkF}
		feeds.insert(doc)
		
	dataI = datetime.datetime(2013, 9, 16)
	dataF = datetime.datetime(2013, 9, 17)
	totalHoje = feeds.find({'data':{'$gte': dataI, '$lt': dataF}}).count()
	return totalHoje
	
# --- FIM BLOCO DE CODIGO PARA ARMAZENAR AS HEADLINES ---#

# --- BLOCO DE CODIGO PARA TRATAR A DATA DOS FEEDS ---#
def trataDataFeed(data,hora):
	mesesEn = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
	mesesPt = ['Jan','Fev','Mar','Abr','Mai','Jun','Jul','Ago','Set','Out','Nov','Dez']
	data = data.split()[1:4]
	if data[1] in mesesEn:
		data[1] = '0' + str(mesesEn.index(data[1])+1)
	else:
		data[1] = '0' + str(mesesPt.index(data[1])+1)
	hora = hora.split(':')
	try:
		data = datetime.datetime(int(data[2]), int(data[1]), int(data[0]),int(hora[0]),int(hora[1]),int(hora[2]))
	except:
		data = datetime.datetime(int(data[2]), int(data[1]), int(data[0]))
	return data
# --- FIM BLOCO DE CODIGO PARA TRATAR A DATA DOS FEEDS ---#

recorrencia = 10000 # Quantidade de vezes que os termos serão buscados
tempo_espera = 300 # Tempo de espera entre uma busca e outra (em segundos)
totalHoje = 0

feedSource = ['internacionalE',
			'aemercadosE',
			'economiaE',
			'negociosE',
			'googleNegocios',
			'uolEconomia',
			'acoesInfomoney',
			'acoesIndicesInfomoney',
			'cambioInfomoney',
			'mercadosInfomoney',
			'cnnEconomy',
			'cnnMarkets',
			'nytEconomy',
			'wsjMarkets',
			'reutersEconomy',
			'reutersUSDollar']



def feadReader():
	for l in range(1,recorrencia+1):
	
		feedLink = [feedparser.parse('http://estadao.feedsportal.com/c/33043/f/534108/index.rss'),
			feedparser.parse('http://economia.estadao.com.br/EN/rss/aemercados.xml'),
			feedparser.parse('http://economia.estadao.com.br/EN/rss/economia.xml'),
			feedparser.parse('http://economia.estadao.com.br/EN/rss/negocios.xml'),
			feedparser.parse('https://news.google.com/news/feeds?pz=1&cf=all&ned=pt-BR_br&hl=pt-BR&topic=b&output=rss'),
			feedparser.parse('http://rss.uol.com.br/feed/economia.xml'),
			feedparser.parse('http://www.infomoney.com.br/onde-investir/acoes/rss'),
			feedparser.parse('http://www.infomoney.com.br/mercados/acoes-e-indices/rss'),
			feedparser.parse('http://www.infomoney.com.br/mercados/cambio/rss'),
			feedparser.parse('http://www.infomoney.com.br/mercados/rss'),
			feedparser.parse('http://rss.cnn.com/rss/money_news_economy.rss'),
			feedparser.parse('http://rss.cnn.com/rss/money_markets.rss'),
			feedparser.parse('http://rss.nytimes.com/services/xml/rss/nyt/Economy.xml'),
			feedparser.parse('http://online.wsj.com/xml/rss/3_7031.xml'),
			feedparser.parse('http://feeds.reuters.com/news/economy'),
			feedparser.parse('http://feeds.reuters.com/reuters/USdollarreportNews')]
		
		i = 0
		for each in feedLink:
			print feedSource[i]
			print 
				
			for entry in each.entries:
				try:
					a = unicodedata.normalize('NFKD', entry.title).encode('ascii','ignore')
					b = unicodedata.normalize('NFKD', entry.published).encode('ascii','ignore')
					c = unicodedata.normalize('NFKD', entry.link).encode('ascii','ignore')
					d = unicodedata.normalize('NFKD', entry.published.split()[4]).encode('ascii','ignore')
					e = trataDataFeed(b,d)
					totalHoje = writeHeadlines(a,e,c)
					
				except:
					print '--- ERRO NA ABERTURA DO FEED ---', sys.exc_info()[0]
					continue
			i += 1
		
		if (l != recorrencia):
			print '-----------------------------------------------------------------------'
			print 'Aguardando a proxima busca daqui a ' + str(tempo_espera) + ' segundos.'
			print 'A busca ja foi realizada ' + str(l) + ' vez(es).'
			print '-----------------------------------------------------------------------'


			except:
				print 'Erro Inesperado:',sys.exc_info()[0]
				print 'Continuando a coleta!'
				continue
			time.sleep(tempo_espera)
	l += 1


feadReader()



