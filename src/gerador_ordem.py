import pandas as pd
import random
import osmnx as ox
from carregar_grafos import load_graph



def gerador_ordens(grafo, qtd_pedidos):
    lista_de_nos = list(grafo.nodes)
    nos_sorteados = random.sample(lista_de_nos, qtd_pedidos)
    lista_nos_sorteados = []
    for sorteados in nos_sorteados:
        inicio = random.randint(a=8, b=16)
        dados = {'nodeid':sorteados,
         'lat':grafo.nodes[sorteados]['x'],
         'lon': grafo.nodes[sorteados]['y'],
         'peso_kg':random.randint(a=1, b=30),
         'janela_inicio':inicio,
         'janela_fim':inicio + 2
         }
        lista_nos_sorteados.append(dados)
    dados = pd.DataFrame(lista_nos_sorteados)
    return dados
