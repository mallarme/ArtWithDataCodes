#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  pyGraph
#  
#  Copyright 2014 Leandro <Leandro@leandrowar>
#  
import networkx as nx
import matplotlib.pyplot as plt

#A entrada do grafo deve ser um array com as conexões da rede
graph = [
		('Green Bay Packers','Miami'),
		('New York Jets','Miami'),
		('Baltimore Colts','Miami'),
		('Pittsburgh Steelers','Miami'),
		('Pittsburgh Steelers','Miami'),
		('San Francisco 49ers','Miami'),
		('San Francisco 49ers','Miami'),
		('Denver Broncos','Miami'),
		('Kansas City Chiefs','New Orleans'),
		('Dallas Cowboys','New Orleans'),
		('Pittsburgh Steelers','New Orleans'),
		('Dallas Cowboys','New Orleans'),
		('Oakland Raiders','New Orleans'),
		('Chicago Bears','New Orleans'),
		('San Francisco 49ers','New Orleans'),
		('Green Bay Packers','New Orleans'),
		('New England Patriots','New Orleans'),
		('Baltimore Ravens','New Orleans')
		]

#Função para criar o grafo
def draw_graph(graph,
               node_size=100, node_color='red', node_alpha=0.5,
               node_text_size=12,
               edge_color='blue', edge_alpha=0.8, edge_tickness=1,
               edge_text_pos=0.3,
               text_font='sans-serif'):

    # Cria o grafo
    G=nx.Graph()

    #Cria as conexões entre os nós
    for edge in graph:
        G.add_edge(edge[0], edge[1])
	
	#Layout da rede
	graph_pos=nx.spring_layout(G)

    # Plot os grafos
    nx.draw_networkx_nodes(G,graph_pos,node_size=node_size, 
                           alpha=node_alpha, node_color=node_color)
    nx.draw_networkx_edges(G,graph_pos,width=edge_tickness,
                           alpha=edge_alpha,edge_color=edge_color)
    nx.draw_networkx_labels(G, graph_pos,font_size=node_text_size,
                            font_family=text_font)

    #Plotando...
    plt.show()

#Chamada da função
draw_graph(graph)

