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
