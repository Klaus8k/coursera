ma = [[0 for i in range(10)] for _ in range(10)]
ma[5][7] = 4
ma[5][5] = -4
x = []
for i in range(len(ma)):
    x=[]
    for j in range(len(ma)):
        x.append(ma[i][j])

    print(x)