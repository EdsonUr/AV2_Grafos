import heapq
primFile = open('prim.txt', 'r')
primNumVertices = int(primFile.readline())

# G = [V, E] && w = matrix of weights && r = root
G = [] ##GRAPH
V = [] ##VERTICES
E = [] ##EDGES
w = [] ##WEIGHTS

for vertice in range(primNumVertices):
    V.append(vertice)
    w.append([0] * primNumVertices)
    rowEdges = [float(x) for x in primFile.readline().split()]

    for edge in rowEdges:
        if edge != 0:
            E.append([vertice, rowEdges.index(edge)])
            w[vertice][rowEdges.index(edge)] = edge

r = int(primFile.readline()) - 1 ##ROOT
G.append(V)
G.append(E)

##Key = menor valor possivel para chegarmos ao vertice
##pi = vertice pai

def Adj(G,u):
    adj = []
    for edge in G[1]:
        if(edge[0] == u):
            adj.append(edge[1])
    return adj

def prim(G, w, r):
    V = G[0]
    E = G[1]
    key = []
    pi = []

    for vertice in V:
        key.append(float('inf'))
        pi.append(None)

    key[r] = 0
    pi[r] = -1
    Q = [(key[v], v) for v in range(len(V))]
    heapq.heapify(Q)
    vertices_in_heap = set(v for key, v in Q)

    while Q:
        u = heapq.heappop(Q) ##Vertice com menor key
        vertices_in_heap.remove(u[1])

        adj = Adj(G, u[1])
        for v in adj:
            if v in vertices_in_heap and w[u[1]][v] < key[v]:
                pi[v] = u[1]
                key[v] = w[u[1]][v]

                print("PI: ",pi)
                print("key: ",key)
        
    if None in pi:
        print(False)
        print("Grafo desconexo")
    else:
        print(True)
        for i in range(len(pi)):
            if(pi[i] != -1):
                pi[i] += 1
        print(pi)
     
prim(G, w, r)