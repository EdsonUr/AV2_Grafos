bellFile = open('bf.txt', 'r')
bellNumVertices = int(bellFile.readline())

G = [] ##GRAPH
V = [] ##VERTICES
E = [] ##EDGES
w = [] ##WEIGHTS

for vertice in range(bellNumVertices):
    V.append(vertice)
    w.append([0] * bellNumVertices)
    rowEdges = [float(x) for x in bellFile.readline().split()]

    for edge in rowEdges:
        if edge != 0:
            E.append([vertice, rowEdges.index(edge)])
            w[vertice][rowEdges.index(edge)] = edge

s = int(bellFile.readline())##ROOT
G.append(V)
G.append(E)

def iniciaOrigemUnica(G, s):
    V = G[0]
    d = []
    pi = []

    for vertice in V:
        d.append(1000000)
        pi.append(None)

    d[s] = 0
    pi[s] = -1

    return d, pi

def relax(u, v, w, d, pi):
    if d[v] > d[u] + w[u][v]:
        d[v] = d[u] + w[u][v]
        pi[v] = u

def bellmanFord(G, w, s):
    d, pi = iniciaOrigemUnica(G, s)
    for i in range(len(G[0]) - 1):
        for edge in G[1]:
            relax(edge[0], edge[1], w, d, pi)
    for edge in G[1]:
        if d[edge[1]] > d[edge[0]] + w[edge[0]][edge[1]]:
            return {'success': False}  # Indica a presença de um ciclo negativo
    return {'success': True, 'distances': d, 'predecessors': pi}



print(bellmanFord(G, w, s))