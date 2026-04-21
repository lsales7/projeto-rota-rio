# Rota Rio

Otimização de rotas de entrega para transportadoras urbanas no Rio de Janeiro, usando dados reais de malha viária e o algoritmo de Vehicle Routing Problem (VRP).

---

## O problema

Do lado do cliente final, o que mais irrita é quando a encomenda não chega no prazo. Do lado das transportadoras, a dor é a margem apertada causada por frete defasado, combustível caro e operação ineficiente. O RotaRio ataca exatamente esse segundo problema: dado um conjunto de pedidos com peso e janela de horário, como distribuir as entregas entre uma frota heterogênea de forma a minimizar o tempo total de entrega?

---

## Como funciona

O projeto é composto por quatro módulos que funcionam em cadeia.

**`carregar_grafo.py`** -> Baixa o grafo viário do Rio de Janeiro via OpenStreetMap usando OSMnx. Implementa um sistema de cache local: na primeira execução faz o download e salva em disco; nas seguintes, carrega direto do arquivo `.pkl` sem acessar a rede.

**`gerador_ordem.py`** -> Gera pedidos sintéticos sobre nós reais da malha viária. Cada pedido tem coordenadas reais (lat/lon), peso aleatório em kg e uma janela de horário para entrega. Os pontos de entrega são sorteados diretamente do grafo, garantindo que todo endereço gerado existe numa rua real do Rio.

**`vrp_solucao.py`** -> O coração do projeto. Distribui os pedidos entre os veículos da frota usando o algoritmo First Fit com cálculo de tempo de viagem real via NetworkX. Para cada pedido, calcula o caminho mais curto em segundos usando os atributos de `travel_time` nas arestas do grafo, respeitando a capacidade máxima de cada veículo.

**`visualizador_rotas.py`** -> Gera um mapa interativo em HTML com Folium, renderizado sobre o OpenStreetMap. Cada tipo de veículo aparece em uma cor diferente. O galpão base em Duque de Caxias é marcado como ponto de origem de todas as rotas.

---

## A frota simulada

O projeto modela uma frota heterogênea baseada nos veículos reais usados por transportadoras brasileiras.

| Tipo | Capacidade | Cor no mapa | Perfil de uso |
|------|-----------|-------------|---------------|
| Van/Utilitário | 1.000 kg | Azul | Centro histórico, Zona Sul, ruas estreitas |
| VUC | 2.500 kg | Verde | Núcleo da operação urbana |
| Caminhão 3/4 | 6.000 kg | Vermelho | Zona Norte, Zona Oeste, Baixada |

O depósito de origem está localizado na **Rodovia Washington Luís, Duque de Caxias** — região onde se concentram os principais centros de distribuição que atendem o Rio de Janeiro.

---

## Bibliotecas

- **OSMnx** — Download e processamento do grafo viário real do Rio de Janeiro via OpenStreetMap
- **NetworkX** — Cálculo de caminhos mais curtos ponderados por tempo de viagem
- **Folium** — Geração do mapa interativo em HTML
- **Pandas** — Estruturação e manipulação dos dados de pedidos
- **scikit-learn** — Dependência do OSMnx para busca de nós em grafos não projetados
- **pickle** — Serialização do grafo para cache local

---

## Estrutura do projeto

```
RotaRio/
├── data/
│   ├── raw/
│   │   └── rj_grafo.pkl        # Grafo viário do Rio (gerado na primeira execução)
│   │   └── mapa_rotas.html     # Mapa interativo gerado pelo visualizador
├── src/
│   ├── carregar_grafos.py      # Download e cache do grafo OSMnx
│   ├── gerador_ordem.py        # Geração de pedidos sintéticos
│   ├── solucionar_rotas.py     # Algoritmo VRP e cálculo de tempo de viagem
│   └── visualizador.py         # Mapa interativo com Folium
├── notebooks/                  # Exploração e análise
└── requirements.txt
```

---

## Instalação

```bash
git clone https://github.com/seu-usuario/rotario.git
cd rotario
pip install -r requirements.txt
```

**Dependências:**

```
osmnx
networkx
folium
pandas
scikit-learn
```

---

## Como executar

Execute os módulos em sequência a partir da raiz do projeto.

**1. Baixar o grafo do Rio de Janeiro**
```bash
python src/carregar_grafos.py
```
Na primeira execução faz o download completo.

**2. Gerar e visualizar as rotas**
```bash
python src/visualizador.py
```
Gera os pedidos, distribui entre a frota e salva o mapa em `data/raw/mapa_rotas.html`. Abra o arquivo no navegador para visualizar as rotas interativas.

---

## Resultado

O mapa gerado mostra os pontos de entrega distribuídos pela malha viária real do Rio de Janeiro, com cada veículo representado por uma cor. O galpão base em Duque de Caxias é o ponto de origem de todas as rotas.

Em um cenário com 500 pedidos e a frota padrão, o algoritmo distribui as entregas priorizando veículos menores — o que reflete o comportamento real das transportadoras urbanas, onde VUCs e vans absorvem a maior parte das entregas dentro dos limites de restrição de circulação do município.

---

## Contexto regulatório

O Rio de Janeiro possui restrições de circulação para veículos de carga definidas pelo **Decreto Municipal 45.433/2018**. VUCs (largura máxima de 2,50m e comprimento de 7,20m) são os únicos autorizados a circular no Centro e Zona Sul no horário comercial. Caminhões maiores ficam restritos ao período noturno nessas áreas. O projeto considera esse contexto na definição da frota simulada.

---

## Próximos passos

- Análise comparativa entre rota otimizada e distribuição aleatória, quantificando a economia de tempo;
- Implementação do algoritmo Nearest Neighbor para seleção geográfica do veículo mais próximo de cada pedido;
- Respeito às janelas de horário de entrega como restrição hard no algoritmo;
- Modelagem das restrições de circulação por zona e horário.

---

Lucas Sales
---
Linkedin: https://www.linkedin.com/in/lucas-sales7/
