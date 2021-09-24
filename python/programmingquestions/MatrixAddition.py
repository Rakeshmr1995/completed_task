x = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
y = [[3, 2, 1],
     [6, 5, 4],
     [8, 7, 3]]
result = [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]]
for i in range(len(x)):
    for j in range(len(x[0])):
        result[i][j]=x[i][j]+y[i][j]
for r in result:
    print(r)