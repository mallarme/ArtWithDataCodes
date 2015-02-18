#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  apriori.py
#  
#  Copyright 2015 Leandro <Leandro@leandrowar>
#  

from collections import Counter
import itertools
import sys

#Parâmetros de suporte e confiança
s = 0.25
c = 0.5

#Conjunto de transações
transacoes = {	1: {"Cerveja", "Amendoim", "Laranja"},
				2: {"Cerveja", "Cafe", "Laranja", "Amendoim"},
				3: {"Cerveja", "Laranja", "Ovos"},
				4: {"Cerveja", "Amendoim", "Ovos", "Leite"},
				5: {"Cafe", "Laranja", "Ovos", "Leite"},
				6: {"Cafe", "Laranja", "Ovos", "Leite"},
				7: {"Laranja", "Cafe", "Cerveja", "Ovos"},
				8: {"Amendoim", "Cafe", "Cerveja", "Ovos"},
				9: {"Amendoim", "Laranja", "Cerveja", "Ovos"},
				10: {"Amendoim", "Cafe", "Cerveja", "Ovos"}
				}

#Faz a leitura do dicionário de transações
#Armazena cada item no vetor items
items = [] 
for itemsets in transacoes.values():
    for item in itemsets:
        items.append(item)
items = set(items)

### Cria as regras de associação ##############################
def frequentItems(items, trans, n, s):
    itemsets = set(itertools.combinations(items, n))

    itemTransactions = []
    for i in itemsets:
        for k,v in transacoes.items():
            if set(v).intersection(set(i)) == set(i):
                itemTransactions.append(i)

    ret = []
    for k,v in sorted(Counter(itemTransactions).items()):
        if v >= s * len(trans):
            ret.append([k, v])
    return(dict(ret))
###############################################################

#Mostra os resultados
print("1-itemsets mais frequentes:")
print(frequentItems(items, transacoes, 1, s))
print

print("2-itemsets mais frequentes:")
print(frequentItems(items, transacoes, 2, s))
print

print("3-itemsets mais frequentes:")
print(frequentItems(items, transacoes, 3, s))
print

#Imprime as regras de associação
#De acordo com o suporte e confiança
print("Regras de associacao com suporte")
print("e confianca maiores que 50%")
f2 = frequentItems(items, transacoes, 2, s)
k2 = [k for k in f2.keys()]
v2 = [v for v in f2.values()]

f1 = frequentItems(items, transacoes, 1, s)
k1 = [k[0] for k in f1.keys()]
v1 = [v    for v in f1.values()]

for i in range(len(k2)):
    i1 = k2[i][0]
    i2 = k2[i][1]
    for j in range(len(k1)):
        if k1[j] == i1:
            confidence = v2[i]/v1[j]
    if v2[i] >= s * len(transacoes) and confidence >= c:
        print("{0:<6} -> {1:<6}: ({2},{3})".format(i1, i2,str(v2[i]),confidence))
    
    i1 = k2[i][1]
    i2 = k2[i][0]
    for j in range(len(k1)):
        if k1[j] == i1:
            confidence = v2[i]/v1[j]
    if v2[i] >= s * len(transacoes) and confidence >= c:
        print("{0:<6} -> {1:<6}: ({2},{3})".format(i1, i2,str(v2[i]),confidence))
        print
