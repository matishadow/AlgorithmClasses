def add(number1, number2):
    result = []

    c = 0
    for bit in range(len(number1) - 1, -1, -1):
        r = number1[bit] + number2[bit] + c

        if r == 0 or r == 1:
            result.insert(0, r)
            c = 0
        elif r == 2 or r == 3:
            result.insert(0, r - 2)
            c = 1

    if c == 1:
        result.insert(0, c)

    return result


def multiply(number1, number2):
    n = len(number1)
    result = [0] * (2 * n)

    for i in range(n):
        r = [0] * (2 * n)
        for j in range(n):
            r[len(r) - i - j - 1] = number1[n - j - 1]

        if number2[n - i - 1] != 0:
            result = add(result, r)

    return result


def divide(x, y):
    q = 0
    r = x
    b = y

    if x < y:
        return q, r

    while b <= x:
        b *= 2

    while b != y:
        b //= 2
        q *= 2

        if r >= b:
            r -= b
            q += 1

    return q, r


def mode_xp(x, y, N):
    f = 1
    z = x

    if y == 0:
        return f

    while y != 0:
        if y % 2 != 0:
            f = f * z % N
        y //= 2
        z = (z * z % N)

    return f
