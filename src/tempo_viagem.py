import networkx as nx
import osmnx as ox
from carregar_grafos import load_graph

def calcular_tempo_viagem(grafo, origem, destino):
    try:
        distancia = nx.shortest_path_length(grafo, origem, destino, weight='travel_time')/60
    except nx.NetworkXNoPath:
        return float('inf')
    return distancia




