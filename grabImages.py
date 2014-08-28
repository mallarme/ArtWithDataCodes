#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  grabImages.py
#  
#  Copyright 2014 Leandro <Leandro@leandrowar>

from bs4 import BeautifulSoup
from urllib2 import urlopen
import urllib


def html(url):
    html = urlopen(url).read()
    return BeautifulSoup(html)

def get_images(url):
    soup = html(url)
    images = [img for img in soup.findAll('img')]
    print (str(len(images)) + "Imagens Econtradas.")
    print 'Copiando as imagens para seu diretorio'
    image_links = [each.get('src') for each in images]
    for each in image_links:
        filename=each.split('/')[-1]
        urllib.urlretrieve(each, filename)
    return image_links


for i in range(1,11):
	get_images('http://thelisticles.net/most-enigmatic-places-on-earth/4589/'+str(i)+'/')
	print 'Download da imagem ' + str(i)

