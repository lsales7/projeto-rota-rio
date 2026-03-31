# Importando bibliotecas
import osmnx as ox
import pickle
from pathlib import Path


#Criando função para salvar o arquivo

def download_graph(caminho):
    estado = ox.graph_from_place("Rio de Janeiro, Brazil", network_type='drive') # mapeia vias no qual apenas o veículos urbanos podem transitar
    estado = ox.add_edge_speeds(estado) # calcula a velocidade das vias do rio de janeiro
    estado = ox.add_edge_travel_times(estado) # calcula o tempo de viagem baseado no local e velocidade do rio de janeiro
    with open(caminho, "wb") as rj_grafo:
        pickle.dump(estado, rj_grafo) # Salva o grafo em arquivo .pkl, não perdendo o formato. 
    return estado
    


# Criando função para carregar o arquivo pkl
def load_graph(caminho): # Criar a função para carregar o .pkl
    if Path(caminho).exists():# verifica se o arquivo já existe na pasta
        with open(caminho, "rb") as arquivo: #abre o arquivo
            grafo = pickle.load(arquivo) #carrega o arquivo na variavel grafo
        return grafo # retorna com o .pkl
    else:
        return download_graph(caminho) # Caso contrário, ele baixa.



if __name__ == '__main__':
    caminho = "data/raw/rj_grafo.pkl"  #definir o caminho no qual o arquivo está
    grafo_rj = load_graph(caminho) #atribui a variavel grafo_rj ao carregar o arquivo
    arestas = len(grafo_rj.edges) #arestas do grafo
    nos = len(grafo_rj.nodes) #nós do grafo
    print(f"Quantidade de nós:{nos}") #printa a quantidade de nós 
    print(f"Quantidade de arestas:{arestas}") #printa a quantidade de arestas



