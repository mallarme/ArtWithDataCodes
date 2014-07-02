#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  regLog.py
#  
import numpy as np
import matplotlib as plt

from sklearn import datasets #diversas bases de dados pre-carregadas
from sklearn import metrics
from sklearn.linear_model import LogisticRegression

#Carrega a base de dados iris em uma instância chamada dataset
dataset = datasets.load_iris()

model.fit(dataset.data, dataset.target) #modulo para construcao do modelo - model.fit (X, Y)

#Comparacao do valor esperado com o valor predito
expected = dataset.target
predicted = model.predict(dataset.data)

print (metrics.classification_report(expected, predicted))
print (metrics.confusion_matrix(expected, predicted))
