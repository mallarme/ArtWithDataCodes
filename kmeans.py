#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  kmeans.py
#  
#  Copyright 2014 Leandro <Leandro@leandrowar>
#  
from pylab import plot,show,title,xlabel,ylabel
from numpy import vstack,array
from numpy.random import rand
from scipy.cluster.vq import kmeans,vq


#Dados do treino
#no formato [lance livre, tempo relogio]
 
					#sab	#dom	#seg	#ter	#sex	#dom	#seg	#ter
data = vstack(array([[7,20],[15,22],[19,20],[16,24],[12,15],[15,10],[20,15],[19,14]]))

# Calculando o K-means, com 2 clusters
centroids,_ = kmeans(data,2)

# Relacionando os pontos com os clusters
idx,_ = vq(data,centroids)

# Grafico
plot(data[idx==0,0],data[idx==0,1],'ob',
     data[idx==1,0],data[idx==1,1],'or')
plot(centroids[:,0],centroids[:,1],'sg',markersize=8)
title('K-means com numpy')
xlabel('Acertos em 70 lances livres')
ylabel('Tempo relogio')
show()


def main():
	
	return 0

if __name__ == '__main__':
	main()

