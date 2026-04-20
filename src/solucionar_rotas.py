#Importar bibliotecas
import pandas as pd
import osmnx as ox
import networkx as nx
from carregar_grafos import load_graph
from gerador_ordem import gerador_ordens
from tempo_viagem import calcular_tempo_viagem

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
] #Dicionário representando a frota de veículos disponíveis para entrega, com suas capacidades e cargas atuais.

def distribuir_pedidos_veiculos(grafo, pedidos, frota, galpao_base): #função para resolver o problema de rotas
    for indice, pedido in pedidos.iterrows(): #percorre sobre cada pedido no dataframe
        tempo = calcular_tempo_viagem(grafo, galpao_base, pedido['nodeid']) #calcula o tempo de viagem do galpao até o local do pedido
        for veiculo in frota: #percorre sobre cada veículo da frota verificando se o pedido pode ser carregado com base na capacidade do veículo e no peso atual
            if veiculo['carga_atual'] + pedido['peso_kg'] <= veiculo['capacidade_kg']:
                 pedido['tempo_viagem'] = tempo
                 veiculo['pedidos'].append(pedido)
                 veiculo['carga_atual'] = pedido['peso_kg'] + veiculo['carga_atual']
                 break
    return frota
                

if __name__ == "__main__": #modulo principal para execução do código
    g = load_graph("data/raw/rj_grafo.pkl") #carrega o grafo do Rio de Janeiro
    galpao_base = ox.distance.nearest_nodes(g, X=-43.311, Y=-22.785) #Coordenada da base de operações
    pedidos = gerador_ordens(grafo=g, qtd_pedidos=500) #Gerador de pedidos, criando um DF
    programacao = distribuir_pedidos_veiculos(grafo=g, pedidos=pedidos, frota=frota, galpao_base=galpao_base) #função para resolver o problema de rota, carregando os pedidos nos veículos da frota
    for programacoes in programacao:
        print(f"Veículo: {programacoes['tipo']} | Carga: {programacoes['carga_atual']}kg | Pedidos: {len(programacoes['pedidos'])}") #imprime o titpo de veículo e a capacidade atual de carga 
        
    
        
            
                
                


            

