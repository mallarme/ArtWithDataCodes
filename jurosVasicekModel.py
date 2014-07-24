#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  jurosVasicekModel.py
#  
#  Copyright 2014 Leandro <Leandro@leandrowar>

import numpy as np
from numpy.random import standard_normal
from numpy import array, zeros, sqrt, shape
from pylab import plot, title, xlabel, ylabel, show, figure, grid

selic = 11.		# Taxa Selic atual
theta = 10.74	# TJ6
k = 0.3
beta = 0.11		# Selic média
 
#Parametros iniciais
n = 5		# Número de simulacoes
T = 6.		# TJ6 - tempo da taxa de juros de referencia de 6 meses
m = 100.	# interacoes
dt = T/m	# taxa para cada interacao
 
tx_cp = np.zeros(shape=(n, m), dtype=float) # matriz que armazena as taxas

fig1 = figure(1)
fig1.clf()

for j in np.arange(0,n): # numero de simulacoes de MC
	tx_cp[j,0] = selic
	for i in np.arange(1,m): #tentativas por simulacao				
		tx_cp[j,i] = tx_cp[j,i-1] + k*(theta-tx_cp[j,i-1])*dt + beta*sqrt(dt)*standard_normal();		
        plot(np.arange(0, T, dt), tx_cp[j])		
 
# Plot das simulacoes
t = np.arange(0, T, dt)
tx_esperada = theta + (selic-theta)*pow(np.e,-k*t)
tx_desvio = sqrt( pow(beta,2)/(2*k)*(1-pow(np.e,-2*k*t)))

plot(np.arange(0, T, dt), tx_esperada, '-r')
plot(np.arange(0, T, dt), tx_esperada+2*tx_desvio, '-b')
plot(np.arange(0, T, dt), tx_esperada-2*tx_desvio, '-b')


title('Modelo de Vasicek para a TJ6' )
xlabel('Meses')
ylabel('Juros nos proximos 6 meses')
grid()

taxa_final = tx_cp[:,-1]
print 'Media final observada: ', np.mean(taxa_final)

show()
