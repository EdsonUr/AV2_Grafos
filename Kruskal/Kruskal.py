import heapq

kruskalFile = open('kruskal.txt', 'r')
kruskalNumEdges = int(kruskalFile.readline())
kruskaEdgesWeight = [float(x) for x in kruskalFile.read().split()]
kruskalFontEdge = int(kruskaEdgesWeight.pop(-1))

def adjustMatrix(vectorEdgesWeight):
    matrix = []
    for i in range(kruskalNumEdges):
        row = []
        for j in range(kruskalNumEdges):
            edgeWeigth = vectorEdgesWeight.pop(0)
            if(edgeWeigth != 0):
                row.append([edgeWeigth, i, j])
        if(len(row) != 0):
            matrix.append(row)
    return matrix

def sortEdges(matrix):
    sortedEdges = []
    for row in matrix:
        for edge in row:
            sortedEdges.append(edge)
    sortedEdges.sort(key=lambda x: x[0])
    return sortedEdges

def makeSet(numEdges):
    sets = [[] * numEdges for i in range(numEdges)]
    belongsTo = []
    for i in range(numEdges):
        sets[i].append(i)
        belongsTo.append(i)
    return sets, belongsTo

def findSet(belongsTo, edge):
    return belongsTo[edge]

def union(belongsTo, edge1, edge2):
    belongsTo[edge1] = edge2

def kruskal(numEdges, vectorEdgesWeight):
    A = []
    adjustedMatrix = adjustMatrix(vectorEdgesWeight)
    sortedEdges = sortEdges(adjustedMatrix)
    sets, belongsTo = makeSet(numEdges)

    for edge in sortedEdges:
        if(findSet(belongsTo, edge[1]) != findSet(belongsTo, edge[2])):
            A.append(edge)
            union(belongsTo, findSet(belongsTo, edge[1]), findSet(belongsTo, edge[2]))

    
    return A
    

print(kruskal(kruskalNumEdges, kruskaEdgesWeight))
