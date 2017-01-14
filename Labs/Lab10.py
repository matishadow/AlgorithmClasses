def greatest_subset(set):
    result = 0
    n = len(set)

    temp = 0
    for i in range(n):
        if temp > 0:
            temp += set[i]
        else:
            temp = set[i]

        if temp > result:
            result = temp

    return result


def shortest_distance_hotels(distances):
    distances = [0] + distances
    n = len(distances)
    penalties = [0] * n
    path = [0] * n

    for i in range(n):
        for j in range(i):
            temp_penalty = penalties[j] + (200 - (distances[i] - distances[j])) ** 2

            if penalties[i] == 0 or temp_penalty < penalties[i]:
                penalties[i] = temp_penalty
                path[i] = j

    print_path(path, n - 1)
    return path


def print_path(path, i):
    if i == 0: return
    print_path(path, path[i])
    print(i, end=', ')


def max_expected_profit(a, b, k1):
    l_a = len(a)
    l_b = len(b)
    profit = [0] * l_b
    prev = [0] * l_b

    profit[0] = b[0]
    k = k1
    for j in range(1, l_a):
        profit[j] = b[j]
        prev[j] = 0
        for i in range(j - 1):
            if a[j] - a[i] >= k:
                p = profit[i] + b[j]
                if p > profit[j]:
                    profit[j] = p
                    prev[j] = i
    max_profit = profit[0]
    max_index = 0

    for i in range(1, l_a):
        if profit[i] > max_profit:
            max_profit = profit[i]
            max_index = i

    return max_profit, max_index


def levenshtein_distance(x, y):
    m = len(x)
    n = len(y)

    E = [[0 for x in range(n+1)] for y in range(m+1)]

    for i in range(m+1):
        E[i][0] = i
    for j in range(n+1):
        E[0][j] = j

    for i in range(1, m+1):
        for j in range(1, n+1):
            if x[i-1] == y[j-1]:
                diff = 0
            else:
                diff = 1
            E[i][j] = min(E[i - 1][j] + 1, E[i][j - 1] + 1, E[i - 1][j - 1] + diff)

    return E[m][n]
