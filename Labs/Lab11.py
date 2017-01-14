def longest_common_subsequence(X, Y):
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


def joined_lcs_1(X, Y):
    X.insert(0, 0)
    Y.insert(0, 0)
    m = len(X)
    n = len(Y)

    c = [[0 for x in range(m - 1)] for y in range(n + 1)]
    b = [[0 for x in range(m - 1)] for y in range(n + 1)]

    for i in range(m):
        if X[i] == Y[0]:
            c[i][0] = 1
            b[i][0] = "leftup"
        else:
            c[i][0] = 0
            b[i][0] = ""
    for i in range(1, n):
        if X[0] == Y[i]:
            c[0][i] = 1
            b[0][i] = "leftup"
        else:
            c[0][i] = 0
            b[0][i] = ""

    for i in range(1, m):
        for j in range(1, n):
            if X[i] == X[j]:
                if X[i - 1] == Y[j - 1]:
                    c[i][j] = c[i - 1][j - 1] + 1
                    b[i][j] = "leftup"
                else:
                    c[i][j] = max(c[i - 1][j - 1], 1)
                    b[i][j] = ""
            else:
                if c[i - 1][j] >= c[i][j - 1]:
                    c[i][j] = c[i - 1][j]
                    b[i][j] = "up"
                else:
                    c[i][j] = c[i][j - 1]
                    b[i][j] = "left"

    return b, c

