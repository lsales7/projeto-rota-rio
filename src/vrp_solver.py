#Importar bibliotecas
import pandas as pd
import osmnx as ox
import networkx as nx
from carregar_grafos import load_graph
from gerador_ordem import gerador_ordens

frota = [
    {
        'tipo': 'van',
        'capacidade_kg': 1000,
        'carga_atual': 0,
        'pedidos': []
    },
    {
        'tipo': 'van',
        'capacidade_kg': 1000,
        'carga_atual': 0,
        'pedidos': []
    },
    {
        'tipo': 'vuc',
        'capacidade_kg': 2500,
        'carga_atual': 0,
        'pedidos': []
    },
    {
        'tipo': 'vuc',
        'capacidade_kg': 2500,
        'carga_atual': 0,
        'pedidos': [] 
    },
    {
        'tipo': 'vuc',
        'capacidade_kg': 2500,
        'carga_atual': 0,
        'pedidos': []
    },
    {
        'tipo': 'caminhao 3/4',
        'capacidade_kg': 6000,
        'carga_atual': 0,
        'pedidos': []
    },
    {
         'tipo': 'caminhao 3/4',
        'capacidade_kg': 6000,
        'carga_atual': 0,
        'pedidos': []
    }
]

def resolver_vrp(grafo, pedidos, frota):
    for indice, pedido in pedidos.iterrows():
        for veiculo in frota:
            if veiculo['carga_atual'] + pedido['peso_kg'] <= veiculo['capacidade_kg']:
                 veiculo['pedidos'].append(pedido) 
                 veiculo['carga_atual'] = pedido['peso_kg'] + veiculo['carga_atual']
                 break
    return frota
                

if __name__ == "__main__":
    g = load_graph("data/raw/rj_grafo.pkl")
    galpao_base = ox.distance.nearest_nodes(g, X=-43.311, Y=-22.785)
    pedidos = gerador_ordens(grafo=g, qtd_pedidos=500)
    programacao = resolver_vrp(grafo=g, pedidos=pedidos, frota=frota)
    for programacoes in programacao:
        print(f"Veículo: {programacoes['tipo']} | Carga: {programacoes['carga_atual']}kg | Pedidos: {len(programacoes['pedidos'])}")
        
    
        
            
                
                


            

