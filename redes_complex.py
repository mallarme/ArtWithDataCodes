#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  redes_complex.py
#  
#  Copyright 2014 Leandro <Leandro@leandrowar>
#  
# Este programa busca o conteúdo do HTML de todas as noticias do banco feeds
# para verificar quantas vezes os nomes das maiores instituições são citados

#--- IMPORTS DE BIBLIOTECAS ---#

import urllib2
from bs4 import BeautifulSoup
from urlparse import urljoin
import os
import codecs
import unicodedata		#para converter o formato unicode em string
from sys import stdout  #para fazer o print na mesma tela
import pymongo
import sys
from datetime import datetime #para fazer o controle do tempo
import bleach


############# PARAMETROS INICIAIS ###############
#Vetor de instituicoes
#~ inst = ['Brasil','EUA','China','Europa','Europe','Alemanha','Inglaterra','England','USA','United States','Japao','Japan','Germany',
		#~ 'Espanha','Italia','Spain','Italy','Canada','Russia','Brazil']

#G8 = ['Canada','Franca','Alemanha','Italia','Japao','Reino Unido','Inglaterra','Estados Unidos','EUA','Uniao Europeia']
G20 = ['Africa do Sul','Argentina','Brasil','Mexico','Canada','Estados Unidos','EUA','China','Japao','Coreia do Sul','India',
		'Indonesia','Arabia Saudita','Turquia','Uniao Europeia','Alemanha','Franca','Italia','Russia','Reino Unido',
		'Australia','Inglaterra']
G20_I = ['Argentina', 'Australia', 'Brazil', 'Canada', 'China', 'France', 'Germany', 'India', 'Indonesia', 'Italy', 'Japan',
		'Republic of Korea','South Korea', 'Mexico', 'Russia', 'Saudi Arabia', 'South Africa', 'Turkey', 'United Kingdom',
		'England','USA','United States', 'European Union']

#Fontes de noticia para o regex no link
feedSource = ['estadao',
			'uol',
			'cnn',
			'infomoney',
			'nyt',
			'wsj',
			'reuters',
			'nytimes']

fonte = 'googleNews'
conjunto = []

#################################################
	
# Conectando com o Mongo
connection = pymongo.Connection("mongodb://localhost", safe=True)

# handles para a base de dados
db = connection.fia
feeds = db.feeds_copy

query = {}
projection = {'_id':0,"link" : 1 }

try:
	doc = feeds.find(query,projection).skip(2950).limit(300)
	totalLinks = feeds.find(query,projection).count()
	restantes = totalLinks
except:
	print '--- ERRO NO findOne() ---', sys.exc_info()[0]


for each in doc:
	nextLink = each.values()[0]
	#print nextLink
	
	for source in feedSource:
		if source in nextLink:
			fonte = source
	
	print
	print '---------------------------------------------'
	print 'Total de links: ' + str(totalLinks)
	print 'Total de links restantes: ' + str(restantes)
	print '---------------------------------------------'
	print 
	print 'fonte: ' + fonte
	print
	print nextLink
	
	try:
		c=urllib2.urlopen(nextLink)
		soup=c.read( )
		soup = BeautifulSoup(soup)
		soup = soup.find_all('p')
		clean = bleach.clean(soup, tags=[], strip=True)
		clean_padronizado = unicodedata.normalize('NFKD', clean).encode('ascii','ignore')
		#clean_padronizado = 'Este e um teste onde tenho os nomes Brasil, Alemanha e EUA'
		for i in G20:
			if i in clean_padronizado:
				print
				print 'Econtrado pais ' + i
				conjunto.append(i)
			else:
				print 'Nao econtrado pais ' + i
				
		for cada in conjunto:
			for i in range(conjunto.index(cada)+1,len(conjunto)):
				print cada + ' ' + conjunto[i]
				print 'Escrevendo o arquivo de saida'
				print '-----------------------------'
				file = open("redes_complexas.txt", "a") #a - append | w - overwrite
				newLine = cada + '|' + conjunto[i] + '\n'
				try:
					file.write(newLine)
				except:
					print '--- ERRO ---', sys.exc_info()[0]
				file.close()
		conjunto = []

		for i in G20_I:
			if i in clean_padronizado:
				print
				print 'Econtrado pais ' + i
				conjunto.append(i)
			else:
				print 'Nao econtrado pais ' + i
				
		for cada in conjunto:
			for i in range(conjunto.index(cada)+1,len(conjunto)):
				print cada + ' ' + conjunto[i]
				print 'Escrevendo o arquivo de saida'
				print '-----------------------------'
				file = open("redes_complexas.txt", "a") #a - append | w - overwrite
				newLine = cada + '|' + conjunto[i] + '\n'
				try:
					file.write(newLine)
				except:
					'--- ERRO ---', sys.exc_info()[0]
				file.close()
		conjunto = []
		
		restantes = restantes - 1
	
			
	except:
		print '--- ERRO NA ABERTURA DA PAGINA ---', sys.exc_info()[0]

