#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  similarString.py
#  
#  Copyright 2014 Leandro <Leandro@leandrowar>
#  
import difflib
import random

def DNA(length):
    return ''.join(random.choice('CGTA') for nucleot in xrange(length))


DNA1 = DNA(15)
print '-'*45
print 'Sequencia 1'
print '-'*45
print DNA1
print '-'*45
print
DNA2 = DNA(15)
print '-'*45
print 'Sequencia 2'
print '-'*45
print DNA2
print '-'*45
print
print 
 
 
#Modulo o DIFFLIB
s = difflib.SequenceMatcher(None, DNA1, DNA2)

print '-'*45
print 'Retorna a quantidade de caracteres semelhantes'
print '-'*45
print s.find_longest_match(0,len(DNA1),0,len(DNA2)) #Retorna a quantidade de caracteres semelhantes
print '-'*45
print
print '-'*45
print 'Retorna a similaridade, entre 0 e 1'
print '-'*45
print difflib.SequenceMatcher(None, DNA1, DNA2).ratio() #Retorna a prob.
print '-'*45


