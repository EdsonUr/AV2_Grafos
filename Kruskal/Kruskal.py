kruskalFile = open('kruskal.txt', 'r')
kruskalNumEdges = int(kruskalFile.readline())
kruskaEdgesWeight = [float(x) for x in kruskalFile.read().split()]

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
    belongsTo = []
    for i in range(numEdges):
        belongsTo.append(i)

    print("BELONGS TO: ", belongsTo)
    return belongsTo

def findSet(belongsTo, edge):
    print("FIND SET: ", belongsTo[edge])
    return belongsTo[edge]

def union(belongsTo, edge1, edge2):
    for i in range(len(belongsTo)):
        if belongsTo[i] == edge1:
            belongsTo[i] = edge2
    print("UNION: ", belongsTo)
    
def kruskal(numEdges, vectorEdgesWeight):
    A = []
    adjustedMatrix = adjustMatrix(vectorEdgesWeight)
    sortedEdges = sortEdges(adjustedMatrix)
    belongsTo = makeSet(numEdges)

    for edge in sortedEdges:
        print("EDGE: ", edge)
        if(findSet(belongsTo, edge[1]) != findSet(belongsTo, edge[2])):
            A.append(edge)
            union(belongsTo, findSet(belongsTo, edge[1]), findSet(belongsTo, edge[2]))
        
    print(belongsTo)
    if (len(set(belongsTo)) == 1):
        return True, A
    else:
        return False

print(kruskal(kruskalNumEdges, kruskaEdgesWeight))