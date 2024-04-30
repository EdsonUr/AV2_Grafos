kruskalFile = open('kruskal.txt', 'r')
kruskalNumEdges = int(kruskalFile.readline())
kruskaEdgesWeight = [float(x) for x in kruskalFile.read().split()]

def adjustMatrix(vectorEdgesWeight):
    matrix = []
    for i in range(kruskalNumEdges):
        row = []
        for j in range(kruskalNumEdges):
            row.append([float(vectorEdgesWeight.pop(0)), i+1, j+1])
        matrix.append(row)
    return matrix

def kruskal(numEdges, vectorEdgesWeight):
    A = None
    adjustedMatrix = adjustMatrix(vectorEdgesWeight)
    print(adjustedMatrix)
    return A
    

print(kruskal(kruskalNumEdges, kruskaEdgesWeight))
