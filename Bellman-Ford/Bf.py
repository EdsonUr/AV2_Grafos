def read_input(filename):
    with open(filename, 'r') as bellFile:
        bellNumVertices = int(bellFile.readline().strip())

        V = list(range(bellNumVertices))
        E = []
        w = [[float('inf')] * bellNumVertices for _ in range(bellNumVertices)]

        for vertice in range(bellNumVertices):
            rowEdges = [float(x) for x in bellFile.readline().strip().split()]
            for idx, edge in enumerate(rowEdges):
                if edge != 0:
                    E.append([vertice, idx])
                    w[vertice][idx] = edge
        
        s = int(bellFile.readline().strip())
    
    return (V, E), w, s

def iniciaOrigemUnica(G, s):
    V = G[0]
    d = [1000000] * len(V)
    pi = [None] * len(V)

    d[s] = 0
    pi[s] = -1

    return d, pi

def relax(u, v, w, d, pi):
    if d[v] > d[u] + w[u][v]:
        d[v] = d[u] + w[u][v]
        pi[v] = u

def bellmanFord(G, w, s):
    d, pi = iniciaOrigemUnica(G, s)
    for _ in range(len(G[0]) - 1):
        for u, v in G[1]:
            relax(u, v, w, d, pi)
    for u, v in G[1]:
        if d[v] > d[u] + w[u][v]:
            return {'success': False}  # Indica a presença de um ciclo negativo
    return {'success': True, 'distances': d, 'predecessors': pi}

# Leia a entrada do arquivo
G, w, s = read_input('bf.txt')

# Execute o algoritmo de Bellman-Ford
result = bellmanFord(G, w, s)

# Imprima os resultados
if result['success']:
    print("Predecessores:", result['predecessors'])
    print("Distâncias:", result['distances'])
else:
    print("O grafo contém um ciclo negativo.")