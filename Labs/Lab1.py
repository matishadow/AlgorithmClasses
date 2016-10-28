import math


def insertion_sort(array):
    counter = 0

    for j in range(1, len(array)):
        key = array[j]
        i = j - 1

        while i >= 0:
            counter += 1

            if array[i] > key:
                array[i + 1] = array[i]
            else:
                break

            i -= 1

        array[i + 1] = key

    return counter


def insertion_sort_descending(array):
    for j in range(1, len(array)):
        key = array[j]
        i = j - 1

        while i >= 0 and array[i] < key:
            array[i + 1] = array[i]
            i -= 1

        array[i + 1] = key


def find_index(array, value):
    index = None

    for i in range(0, len(array)):
        if array[i] == value:
            index = i
            break

    return index


def factor(n):
    d = 2
    counter = 0

    while d * d <= n:

        counter += 1
        if n % d == 0:
            return counter
        d += 1

    return -1


def egyptian_fraction_decomposition(p, q):
    x1 = p
    y1 = q

    while x1 > 0:
        if y1 % x1 == 0:
            z1 = (y1 // x1)
        else:
            z1 = (y1 // x1) + 1
        print(z1, end=' ')

        x1 = x1 * z1 - y1
        y1 *= z1


def compute_continued_fraction_value(qs):
    q_count = len(qs)

    result = 0

    for i in range(q_count - 1, 0, -1):
        result = 1 / (qs[i] + result)

    result += qs[0]

    return result


def find_continued_fraction(number):
    qs = []
    r = number
    n = 0

    while True:
        an = math.floor(r)
        qs.append(an)
        if r - an == 0:
            break
        else:
            r = 1 / (r - an)
            n += 1
