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

    print_path(path, n)
    return path


def print_path(path, i):
    if i == 0: return
    print_path(path, path[i])
    print(i, end=', ')
