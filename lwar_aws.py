#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  lwar_aws.py
#
#  Copyright 2013 Leandro <Leandro@leandrowar>
#  Fontes:
#	http://aws.amazon.com/articles/Amazon-S3/3998
#	http://boto.s3.amazonaws.com/s3_tut.html


#Imports
import boto.s3
from boto.s3.connection import S3Connection	#para estabelecer a conexão
import sys

#from boto.s3.key import key  #para armazenar dados

# Criando uma conexão com o serviço S3
try:
	conn = S3Connection('AKIAJ4HFAWF3SR4TJ3OQ','L2Zh3lLPmMH4OJoYCgPa6T8KE2FQ7h+C2abHAbuV') #(<aws access key>,<aws secret key>)
	print 'Conexao AWS estabelecida'
except:
	print 'Erro na conexão AWS'
	
# Criando um bucket
try:
	bucket = conn.create_bucket('mi4i.files')
	print
	print 'Bucket mi4i.files criado com sucesso'
except:
	print
	print 'Erro ao criar o bucket'

# Funcao para esperar o upload e o download
def percent_cb(complete, total):
	sys.stdout.write('.')
	sys.stdout.flush()

# Criando a chave para armazenamento e armazenando os dados no S3
try:
	key = bucket.new_key('feedsSecure')	#cria um objeto para o arquivo, mas ainda não há nada armazendo
	key.set_contents_from_filename('‪C:/Users/Leandro/dump/fia/feedsSecure_15042014.metadata.bson',cb = percent_cb, num_cb = 10)
	#abre um handle para o arquivo local, realizando a escrita no objeto chave criado na linha anterior
																
	key.set_acl('public-read') #determina o tipo de controle de acesso
	print
	print 'Arquivo transferido com sucesso'
except:
	print
	print 'Falha na transferencia do arquvio'

#~ # Fazendo o download dos dados
#~ try:
	#~ key = conn.get_bucket('lwar.invest').get_key('certificado')
	#~ key.get_contents_to_filename('C:\mongo_files\download\certificado.pdf',cb = percent_cb, num_cb = 10)
	#~ print 
	#~ print 'Download concluido'
	#~ print
	#~ print
#~ 
#~ except:
	#~ print
	#~ print 'Falha no download'
