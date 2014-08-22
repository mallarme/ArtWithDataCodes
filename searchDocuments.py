#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  searchDocuments.py
#  
#  Copyright 2014 Leandro <Leandro@leandrowar>

from math import log
import os

fileName = []
content = []
sub_dir = "/Python27/docs"


# Lista apenas os arquivos com a extensao .txt
for file in os.listdir(sub_dir):
	if file.endswith(".txt"):
		fileName.append(file.replace('.txt',''))
        for filename in os.listdir(sub_dir):
			f = open(os.path.join(sub_dir, filename), "r")
			for line in f:
				content.append(line)
			f.close()

#Cria um dicionaio com chave = nome do arquivo e valor = conteudo do arquivo
i = 0
documentos = {}
for each in fileName:
	documentos[each] = content[i]
	i = i + 1
	
#Tokeniza dos temos dentro de cada documento
terms = {}
for key in documentos.keys():
	terms[key] = [ i.lower() 
					for i in documentos[key].split()
					]


#Calculo dos scores de frequencia
def tf(termo, doc, normalize=True):
    doc = doc.lower().split()
    if normalize:
        return doc.count(termo.lower()) / float(len(doc))
    else:
        return doc.count(termo.lower()) / 1.0

#Calculo da importancia de cada termo em relacao a todos os documentos
def idf(term, corpus):
    textosTermos = len([True for text in corpus 
							if term.lower() in text.lower().split()
							])
    try:
        return 1.0 + log(float(len(corpus)) / textosTermos)
    except ZeroDivisionError:
        return 1.0

# term frequency–inverse document frequency 
# Calcula o tf-idf
def tf_idf(term, doc, documentos):
    return tf(term, doc) * idf(term, documentos)


#Calcula o score para cada termo da query 

termosBusca = ['Imperio','Luke']

#Inicializa os scores de busca
scoresBusca = {}
for key in documentos.keys():
	scoresBusca[key] = 0

#funcao lower() para padronizar o texto
print '*'*55
for term in [t.lower() for t in termosBusca]:
    for doc in sorted(documentos):
        print 'Score de TF (%s): %s' % (doc, term), tf(term, documentos[doc])
    print 'Importancia IDF: %s' % (term, ), idf(term, documentos.values())
    print
    print '*'*55

	#funcao sorted() para ordernar os documentos

    for doc in sorted(documentos):
        score = tf_idf(term, documentos[doc], documentos.values())
        print 'TF-IDF (%s): %s' % (doc, term), score
        scoresBusca[doc] += score
    print

print '*'*55
print "Score TF-IDF para a busca '%s'" % (' '.join(termosBusca), )
for (doc, score) in sorted(scoresBusca.items()):
    print doc, score
print '*'*55
print
