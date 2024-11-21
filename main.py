from collections import deque

import numpy as np
import random

def generate_graph(n, p):

    """
    - Gera um grafo não direcionado com `n` vértices, onde cada aresta existe com probabilidade `p`

    - Retorna a representação de lista de adjacência e a contagem de arestas
    """

    adjacency_list = {i: [] for i in range(n)}

    edge_count = 0

    for u in range(n):

        for v in range(u + 1, n):

            if random.random() < p:

                adjacency_list[u].append(v)
                adjacency_list[v].append(u)
                edge_count += 1

    return adjacency_list, edge_count

def bfs(graph, start_vertex, n):

    """
    - Implementação da BFS que calcula a distância máxima de um vértice inicial para todos os outros vértices

    - Retorna essa distância máxima 
    """

    colors = ['WHITE'] * n 
    distances = [float('inf')] * n
    parents = [None] * n

    colors[start_vertex] = 'GRAY'
    distances[start_vertex] = 0
    parents[start_vertex] = None

    # Fila BFS
    queue = deque([start_vertex])

    max_distance = 0
    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if colors[v] == 'WHITE':
                colors[v] = 'GRAY'
                distances[v] = distances[u] + 1
                parents[v] = u
                queue.append(v)
                max_distance = max(max_distance, distances[v])
        colors[u] = 'BLACK'

    return max_distance

def compute_graph_properties_with_bfs(adjacency_list, n):

    """
    - Calcula as propriedades de um grafo representado por lista de adjacência
    - Usa a BFS para calcular o diâmetro do grafo

    - Retorna o grau mínimo, grau máximo, grau médio e diâmetro do grafo
    """

    degrees = [len(adjacency_list[v]) for v in range(n)]
    gmin = min(degrees)
    gmax = max(degrees)
    gmed = np.mean(degrees)

    diam = max(bfs(adjacency_list, v, n) for v in range(n) if adjacency_list[v])

    return gmin, gmax, gmed, diam

def generate_graph_and_compute_properties_bfs(ini, fim, stp, p):

    """
    - Gera grafos com `n` variando de `ini` a `fim` com passo `stp` e probabilidade de aresta `p`
    - Calcula as propriedades de cada grafo gerado

    - Retorna uma lista de tuplas com os resultados
    """

    results = []

    for n in range(ini, fim + 1, stp):
        adjacency_list, edge_count = generate_graph(n, p)
        gmin, gmax, gmed, diam = compute_graph_properties_with_bfs(adjacency_list, n)
        results.append((n, edge_count, gmin, gmax, gmed, diam))

    return results