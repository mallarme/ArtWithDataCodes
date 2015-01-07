#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  matrizCorrel.py
#  
#  Copyright 2015 Leandro <leandro.guerra@artedosdados.com.br>
#  

#Bibliotecas
import csv
import pandas as pd
import pandas.io.data
from pandas import Series, DataFrame
pd.__version__
import matplotlib.pyplot as plt
import matplotlib as mpl

#Para remover colunas que não serão utilizadas  
def removeColuna(arquivo):
	arquivo = arquivo
	with open(arquivo,"rb") as source:
	    rdr= csv.reader( source )
	    with open("analise.csv","wb") as result:
	        wtr= csv.writer( result )
	        for r in rdr:
	            wtr.writerow( (r[1],r[6]) )
	return None
	
removeColuna('vale5_cot.csv')

#Importando o CSV para o dataframe
headers = ['Date','Adj Close']
df = pd.read_csv('analise.csv',  index_col='Date', parse_dates=True,names = headers)

#Carrega os precos de fechamento, dentro do periodo selecionado pelo usuario
close_px = df['Adj Close']

###########################################################################################################################
#Calculando a correlacao do papel com outras acoes

arquivo = 'petr4_cot.csv'
#Para remover a coluna papel (primeira) do csv importado do google finance
removeColuna(arquivo)
headers = ['Date','Adj Close']
dfPetr4 = pd.read_csv('analise.csv',  index_col='Date', parse_dates=True,names = headers)

arquivo = 'itub4_cot.csv'
#Para remover a coluna papel (primeira) do csv importado do google finance
removeColuna(arquivo)
headers = ['Date','Adj Close']
dfItub4 = pd.read_csv('analise.csv',  index_col='Date', parse_dates=True,names = headers)

arquivo = 'bbas3_cot.csv'
#Para remover a coluna papel (primeira) do csv importado do google finance
removeColuna(arquivo)
headers = ['Date','Adj Close']
dfBbas3 = pd.read_csv('analise.csv',  index_col='Date', parse_dates=True,names = headers)

arquivo = 'bbdc4_cot.csv'
#Para remover a coluna papel (primeira) do csv importado do google finance
removeColuna(arquivo)
headers = ['Date','Adj Close']
dfBbdc4 = pd.read_csv('analise.csv',  index_col='Date', parse_dates=True,names = headers)


dfCorrel = pd.DataFrame(index=df.index)
dfCorrel['VALE5'] = df['Adj Close']
dfCorrel['PETR4'] = dfPetr4.loc[:,'Adj Close']
dfCorrel['ITUB4'] = dfItub4.loc[:,'Adj Close']
dfCorrel['BBAS3'] = dfBbas3.loc[:,'Adj Close']
dfCorrel['BBDC4'] = dfBbdc4.loc[:,'Adj Close']

###########################################################################################################################
#Calculo das correlacoes dos retornos e criação dos gráficos.
rets3 = dfCorrel[:].pct_change()
corr = rets3.corr()
plt.imshow(corr, cmap='hot', interpolation='none')
plt.colorbar()
plt.xticks(range(len(corr)), corr.columns)
plt.yticks(range(len(corr)), corr.columns);
plt.savefig("correl.png")
plt.show()
