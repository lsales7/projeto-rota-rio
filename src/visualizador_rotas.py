#Importando as bibliotecas necessárias
import folium
import osmnx as ox
from carregar_grafos import carregar_grafo
from gerador_ordem import gerador_ordens
from solucionar_rotas import distribuir_pedidos_veiculos


cores = {
    'van': 'blue',
    'vuc': 'green',
    'caminhao 3/4': 'red'
}

def visualizar_rotas(programacao, galpao_base, grafo):
    mapa_rj = folium.Map(location=[-22.9, -43.2], zoom_start=11) #Cria um mapa do Rio de Janeiro usando a biblioteca Folium, centralizado em coordenadas específicas e com um nível de zoom definido.
    marcador = folium.Marker(location=[grafo.nodes[galpao_base]['y'], grafo.nodes[galpao_base]['x']], popup='Galpão Base - Duque de Caxias', icon=folium.Icon(color='red')) #Adiciona um marcador ao mapa para indicar a localização do galpão base, usando as coordenadas do nó correspondente no grafo.
    marcador.add_to(mapa_rj) #Adiciona o marcador ao mapa.
    for programacoes in programacao:
        for pedido in programacoes['pedidos']:
            folium.CircleMarker(
                location=[pedido['lat'], pedido['lon']], 
                radius=6, color=cores[programacoes['tipo']], 
                popup=f"Pedido: {pedido['nodeid']} | Peso: {pedido['peso_kg']}kg | Janela: {pedido['janela_inicio']}h-{pedido['janela_fim']}h"
                ).add_to(mapa_rj)
    return mapa_rj

if __name__ == '__main__':
    grafo = carregar_grafo(r"data\raw\rj_grafo.pkl")
    galpao = ox.distance.nearest_nodes(grafo, X=-43.311, Y=-22.785)
    pedidos = gerador_ordens(grafo=grafo, qtd_pedidos=gerador_ordens['pedido'])
    distribuir_pedidos = distribuir_pedidos_veiculos(grafo=grafo, pedidos=500, frota=pedidos, galpao_base=galpao)
    mapa = visualizar_rotas(programacao=distribuir_pedidos, galpao_base=galpao, grafo=grafo).save("data/processed/mapa_rotas.html")
    
    