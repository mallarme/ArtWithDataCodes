#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  magicformula.py
#  
#  Copyright 2014 Leandro <Leandro@leandrowar>
#  


import urllib
import re
import datetime
import pymongo
import numpy as np

acoes = ['TRPN3','HBOR3','BRIN3','EZTC3','DIRR3','HGTX3','TAEE11','SCAR3','ETER3','EVEN3']
t1 = datetime.datetime.now()
data = t1.date()
acao = []
cotacao = []
cota_media_dia = []
cota_inicial = [12.99,7.77,6.09,28.32,10.39,24.97,18.88,35.99,8.31,7.63]
data_I = '2014-04-07'
aux = []
aux1 = []
acum_carteira = []
acum_ibov = []

def writeStocks (acao,data,cotacao):
	
	# Conectando com o Mongo
	connection = pymongo.Connection("mongodb://localhost", safe=True)

	# handles para a base de dados
	db = connection.stocks
	magic = db.magic
	
	query = {'data':data,'acao':acao}
	
	doc = None
	try:
		doc = magic.find_one(query)     #Se a cotacao ja existir na base
									  #altera o valor de doc para não haver novo insert
	except:
		print '--- ERRO NO findOne() ---', sys.exc_info()[0]
	
	if (doc == None):
		doc = {'data':data,'acao':acao,'cotacao':cotacao}
		magic.insert(doc)
		
	return None
	
def readStocks (acao,data_I,data):
	
	# Conectando com o Mongo
	connection = pymongo.Connection("mongodb://localhost", safe=True)

	# handles para a base de dados
	db = connection.stocks
	magic = db.magic
	
	query = {'data':data_I,'acao':acao}
	projection = {'_id':0,'cotacao':1}
	
	try:
		doc = magic.find(query,projection)
	except:
		print '--- ERRO NA QUERY ---', sys.exc_info()[0]
	for d in doc:
		aux.append(d.values()[0])	
	
	query = {'data':data,'acao':acao}
	projection = {'_id':0,'cotacao':1}
	
	try:
		doc = magic.find(query,projection)
	except:
		print '--- ERRO NA QUERY ---', sys.exc_info()[0]
	for d in doc:
		aux1.append(d.values()[0])
		
	return None

def get_price(acao):
    fonte = 'http://finance.google.com/finance?q='
    content = urllib.urlopen(fonte + acao).read()
    if acao == 'TRPN3':
		m = re.search('id="ref_920959055355336_l".*?>(.*?)<', content)
		d = re.search('id="ref_920959055355336_cp".*?>(.*?)<', content)
    if acao == 'HBOR3':
		m = re.search('id="ref_634170492010327_l".*?>(.*?)<', content)
		d = re.search('id="ref_634170492010327_cp".*?>(.*?)<', content)
    if acao == 'BRIN3':
		m = re.search('id="ref_143288115589366_l".*?>(.*?)<', content)
		d = re.search('id="ref_143288115589366_cp".*?>(.*?)<', content)		
    if acao == 'EZTC3':
		m = re.search('id="ref_786018950989813_l".*?>(.*?)<', content)
		d = re.search('id="ref_786018950989813_cp".*?>(.*?)<', content)
    if acao == 'DIRR3':
		m = re.search('id="ref_198265296228927_l".*?>(.*?)<', content)
		d = re.search('id="ref_198265296228927_cp".*?>(.*?)<', content)
    if acao == 'HGTX3':
		m = re.search('id="ref_958671418890152_l".*?>(.*?)<', content)
		d = re.search('id="ref_958671418890152_cp".*?>(.*?)<', content)
    if acao == 'TAEE11':
		m = re.search('id="ref_586150771506634_l".*?>(.*?)<', content)
		d = re.search('id="ref_586150771506634_cp".*?>(.*?)<', content)	
    if acao == 'SCAR3':
		m = re.search('id="ref_700207074926583_l".*?>(.*?)<', content)
		d = re.search('id="ref_700207074926583_cp".*?>(.*?)<', content)			
    if acao == 'ETER3':
		m = re.search('id="ref_322584452497829_l".*?>(.*?)<', content)
		d = re.search('id="ref_322584452497829_cp".*?>(.*?)<', content)		
    if acao == 'EVEN3':
		m = re.search('id="ref_701765601815772_l".*?>(.*?)<', content)
		d = re.search('id="ref_701765601815772_cp".*?>(.*?)<', content)		

    if d:
		dia = re.sub('%','',d.group(1))
		dia = dia.strip().strip("()")
    if m:
        cotacao = m.group(1)
    else:
        cotacao = 'Sem informacao disponivel no momento: ' + acao
    writeStocks(acao,str(data),float(cotacao))
    cota_media_dia.append(float(dia))
    return '		' + acao + ':		' + cotacao + '		' + dia + '%', dia
    
def get_ibov(acao):
    fonte = 'http://finance.google.com/finance?q='
    content = urllib.urlopen(fonte + acao).read()
    m = re.search('id="ref_851377182412228_l".*?>(.*?)<', content)
    m2 = re.search('id="ref_851377182412228_cp".*?>(.*?)<', content)
    if m2:
		var_ibov = re.sub('%','',m2.group(1))
		var_ibov = var_ibov.strip().strip("()")
    if m:
        ibov = re.sub(',','',m.group(1))
    else:
        ibov = 'Sem informacao disponivel no momento: ' + acao
    return ibov, var_ibov
 
#Insere os valores iniciais da carteira
for acao in acoes:
	writeStocks (acao,data_I,cota_inicial[acoes.index(acao)])
	writeStocks ('IBOV',data_I,52155)
	writeStocks ('IBOV',str(data),float(get_ibov('ibov')[0]))
 
var_ibov = float(get_ibov('ibov')[1])
   
#Insere e mostra os valores atuais das cotacoes
print
print '-------------------------------------------------------------------'
print 'Cotacoes em ' + str(data) + ': '
print
print '		Acao		Preco		Var(%)'
print
for acao in acoes:
	print get_price(acao)[0]
print
print 'Retorno medio da carteira:	' + str(round(np.mean(cota_media_dia),2)) + '%'
print 'Retorno do Ibovespa:		' + str(var_ibov) + '%'
print 'Retorno da carteira em relacao ao Ibovespa no dia: ' + str(round(np.mean(cota_media_dia)-var_ibov,2)) + '%'
print
print
print 'Entre ' + data_I + ' e ' + str(data) + ':'
print

for acao in acoes:
	readStocks (acao,data_I,str(data))

for each in aux:
	if each/aux1[aux.index(each)] > 0:
		acum_carteira.append(1-each/aux1[aux.index(each)])
	else:
		acum_carteira.append(each/aux1[aux.index(each)]-1)
#reset in aux e aux1
aux = []
aux1 = []

#Read Ibovespa
readStocks ('IBOV',data_I,str(data))
for each in aux:
	if each/aux1[aux.index(each)] > 0:
		acum_ibov.append(1-each/aux1[aux.index(each)])
	else:
		acum_ibov.append(each/aux1[aux.index(each)]-1)

print '        Retorno acumulado da carteira:		' + str(round(np.mean(acum_carteira),4)*100) + '%'
print '        Retorno acumulado do Ibovespa:		' + str(round(np.mean(acum_ibov),4)*100) + '%'
print '        Retorno da carteira em relacao ao Ibovespa:	' + str(round(np.mean(acum_carteira)-acum_ibov,4)*100) + '%'
print '-------------------------------------------------------------------'
print
