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

def compute_graph_properties(adjacency_list, n):

    """
    Computa as propriedades do grafo, incluindo:

    - gmin: grau mínimo

    - gmax: grau máximo

    - gmed: grau médio

    - diam: diâmetro

    Retorna uma tupla com essas propriedades
    """

    # Passo 1: Computar graus dos vértices

    degrees = [len(adjacency_list[v]) for v in range(n)]

    gmin = min(degrees)

    gmax = max(degrees)

    gmed = np.mean(degrees)

    # Passo 2: Computar diâmetro do grafo

    def bfs_diameter(start_vertex):

        visited = [-1] * n

        queue = deque([start_vertex])

        visited[start_vertex] = 0

        max_distance = 0

        while queue:

            current = queue.popleft()

            for neighbor in adjacency_list[current]:

                if visited[neighbor] == -1:

                    visited[neighbor] = visited[current] + 1

                    queue.append(neighbor)

                    max_distance = max(max_distance, visited[neighbor])

        return max_distance

    diam = max(bfs_diameter(v) for v in range(n) if adjacency_list[v])

    return gmin, gmax, gmed, diam