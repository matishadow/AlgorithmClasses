def nwp(X, Y, is_joined):
    X.insert(0, 0)
    Y.insert(0, 0)
    m = len(X)
    n = len(Y)

    c = [[0 for x in range(m - 1)] for y in range(n + 1)]
    b = [[0 for x in range(m - 1)] for y in range(n + 1)]

    for i in range(1, m):
        for j in range(1, n):
            if X[i] == Y[j]:
                c[i][j] = c[i - 1][j-1] + 1
                b[i][j] = "leftup"
            elif c[i - 1][j] >= c[i][j-1]:
                c[i][j] = c[i - 1][j]
                b[i][j] = "up"
            else:
                c[i][j] = c[i][j - 1]
                b[i][j] = "left"

    return b, c
