#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  pdfReport.py
#  
#  Copyright 2014 Leandro <Leandro@leandrowar>
#  
from fpdf import FPDF, HTMLMixin

html = """
	<p align="center"> 
	Primeira String!
	</p> """ +
	#Para inserir uma imagem
	"""
	<center>
	<A HREF="http://icons.iconarchive.com/icons/double-j-design/blueprint/256/adobe-blueprint-pdf-icon.png"><img src="http://icons.iconarchive.com/icons/double-j-design/blueprint/256/adobe-blueprint-pdf-icon.png" width="256" height="256"></A>
	</center>
	""" 

class MyFPDF(FPDF, HTMLMixin):
    pass
 
pdf=MyFPDF()
pdf.alias_nb_pages()
pdf.add_page()
pdf.write_html(html)
pdf.output('pdfReporf.pdf','F')
