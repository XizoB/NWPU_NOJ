dimension = int(input())
inpmatrix = []
for i in range(dimension):
    inpmatrix.append(input().split(' '))

outmatrix = [[0 for i in range(dimension)] for i in range(dimension)]
for i in range(dimension):
    for j in range(dimension):
        outmatrix[dimension-1-j][i] = inpmatrix[i][j]
for i in range(dimension):
    print(" ".join(outmatrix[i]))
