#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  lexical.py
#  
#  Copyright 2014 Leandro <Leandro@leandrowar>
#  
import urllib2
from bs4 import BeautifulSoup
import sys
import unicodedata		#para converter o formato unicode em string
import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter



def divLexica(linkNoticia):
	noticia = ''
	try:
		c = urllib2.urlopen(linkNoticia)
		soup = c.read( )
		soup = BeautifulSoup(soup)
		tags = soup.find_all(['p']) 
		for tag in tags:
			noticia = noticia + ' ' + unicodedata.normalize('NFKD', tag.text).encode('ascii','ignore').lower()
	except:
		print '--- ERRO NA ABERTURA DA PAGINA ---', sys.exc_info()[0]
		
	# --- BLOCO DE CODIGO PARA PRE-PROCESSAMENTO DAS NOTICIAS ---#
	pontos = ['.',',','!','?',';','-','%','$',':','`','´','(',')',"'",'&']
	#Removendo a pontuacao
	for p in pontos:
		noticia = noticia.replace(p, '')
	 
	acentos = ['á','é','í','ó','ú','à','è','ì','ò','ù',
	 'ã','ẽ','ĩ','õ','ũ','â','ê','î','ô','û']
	s_acentos = ['a','e','i','o','u','a','e','i','o','u',
	'a','e','i','o','u','a','e','i','o','u']
	
	for i in range(0, len(acentos)):
		noticia = noticia.replace(acentos[i], s_acentos[i])
	
	#Tokenizacao e Remocao das stopwords
	noticiaProc = [w for w in word_tokenize(noticia) if not w in stopwords.words('portuguese')]
	noticiaProc = [w for w in noticiaProc if not w in stopwords.words('english')]
	
	# --- FIM DO BLOCO DE CODIGO PARA PRE-PROCESSAMENTO DAS HL ---#
	
	# --- BLOCO DE CODIGO PARA CONTAR AS PALAVRAS ---#
	#Contando
	c = Counter(noticiaProc)
	distWords = len(set(noticiaProc)) #conta as palavras distintas
	totalWords = len(noticiaProc) #conta todas as palavras
	c = c.most_common(5)
	return format(float(distWords)/float(totalWords),'0.2f'), c
	
	# --- FIM DO BLOCO DE CODIGO PARA CONTAR AS PALAVRAS ---#

noticia1 = 'http://noticias.uol.com.br/internacional/ultimas-noticias/2014/07/26/israel-aceita-estender-tregua-em-gaza-por-4-horas.htm'
noticia2 = 'http://www1.folha.uol.com.br/mundo/2014/07/1491729-israel-aceita-prolongar-tregua-em-gaza-por-4-horas-diz-tv.shtml'
noticia3 = 'http://www.valor.com.br/internacional/3627678/israel-estende-por-4-horas-tregua-humanitaria-na-faixa-de-gaza'

print 'Diversidade lexica da noticia - UOL: ' + str(divLexica(noticia1)[0])
print 'Diversidade lexica da noticia - FOLHA: ' + str(divLexica(noticia2)[0])
print 'Diversidade lexica da noticia - VALOR: ' + str(divLexica(noticia3)[0])
print
print
print 'Palavras mais frequentes na noticia - UOL: ' + '\n' + str(divLexica(noticia1)[1])
print
print 'Palavras mais frequentes na noticia - FOLHA: ' + '\n' + str(divLexica(noticia2)[1])
print
print 'Palavras mais frequentes na noticia - VALOR: ' + '\n' + str(divLexica(noticia3)[1])
print
print
