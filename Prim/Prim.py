import heapq
primFile = open('prim.txt', 'r')
primNumVertices = int(primFile.readline().strip())

V = [i for i in range(primNumVertices)]
E = []
w = [[0] * primNumVertices for _ in range(primNumVertices)]

for vertice in range(primNumVertices):
    rowEdges = [float(x) for x in primFile.readline().split()]
    for edge_index, edge in enumerate(rowEdges):
        if edge != 0:
            E.append([vertice, edge_index])
            w[vertice][edge_index] = edge

r = int(primFile.readline().strip())  # Raiz
G = [V, E]


def Adj(G, u):
    adj = []
    for edge in G[1]:
        if edge[0] == u:
            adj.append(edge[1])
        elif edge[1] == u:
            adj.append(edge[0])
    return adj

def prim(G, w, r):
    V = G[0]
    key = [float('inf')] * len(V)
    pi = [None] * len(V)
    key[r] = 0
    pi[r] = -1
    
    Q = [(key[v], v) for v in range(len(V))]
    heapq.heapify(Q)
    position = {v: i for i, (_, v) in enumerate(Q)}

    while Q:
        _, u = heapq.heappop(Q)
        position.pop(u, None)

        for v in Adj(G, u):
            if v in position and w[u][v] < key[v]:
                key[v] = w[u][v]
                pi[v] = u
                Q = [(key[vertex], vertex) for _, vertex in Q if vertex in position]
                heapq.heapify(Q)

    if None in pi:
        print("FALSO")
        print("Grafo desconexo")
    else:
        print("VERDADEIRO")
        print(pi)

prim(G, w, r)