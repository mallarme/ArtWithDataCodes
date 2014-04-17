#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  movimento_browniano.py
#  
#  Copyright 2014 Leandro <Leandro@leandrowar>
# 

from numpy.random import standard_normal
from numpy import array, zeros, sqrt, shape
from pylab import *

p_inicial = 15		#preço inicial da ação
H = 1				#parametro para o calcudo da quantidade de passos
dt = 0.002			#tamanho do passo
sigma = 0.2			#volatilidade diária
mu = 0.01			#retono médio diário
nSimu = 2			#número de simulações

passos=round(H/dt); #passos em dias
S = zeros([nSimu, passos], dtype=float)
x = range(0, int(passos), 1)

for j in range(0, nSimu, 1):
        S[j,0]= p_inicial
        for i in x[:-1]:
                S[j,i+1]=S[j,i]+S[j,i]*(mu-0.5*sigma*sigma)*dt+sigma*S[j,i]*sqrt(dt)*standard_normal();
        plot(x, S[j])

title('Simulacao com %d dias e Preco Inicial de %.2f' % (int(passos), p_inicial))
xlabel('Dias')
ylabel('Preco da Acao')
show()
