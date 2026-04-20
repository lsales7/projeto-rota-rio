#Importando as bibliotecas necessárias
import folium
import osmnx as ox


def visualizar_rotas(programacao, galpao_base, grafo):
    mapa_rj = folium.Map(location=[-22.9, -43.2], zoom_start=11) #Cria um mapa do Rio de Janeiro usando a biblioteca Folium, centralizado em coordenadas específicas e com um nível de zoom definido.
    marcador = folium.Marker(location=[grafo.nodes[galpao_base]['y'], grafo.nodes[galpao_base]['x']], popup='Galpão Base - Duque de Caxias', icon=folium.Icon(color='red')) #Adiciona um marcador ao mapa para indicar a localização do galpão base, usando as coordenadas do nó correspondente no grafo.
    marcador.add_to(mapa_rj) #Adiciona o marcador ao mapa.
    for programacoes in programacao:
        
            
            





cores = {
    'van': 'blue',
    'vuc': 'green',
    'caminhao 3/4': 'red'
}

