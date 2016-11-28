import math
import random
import sys


def index_number(array, start_i, end_i):
    middle = int((end_i + start_i) / 2)
    val = array[middle]

    if array[0] > 0 or array[len(array) - 1] < end_i:
        return None

    if val == middle:
        return middle
    elif end_i - start_i == 1:
        return None
    elif val > middle:
        return index_number(array, start_i, middle)
    else:
        return index_number(array, middle, end_i)


def split(array, b):
    l = 0
    r = len(array)

    while l != r:
        if array[l] <= b:
            l += 1
        elif array[r - 1] > b:
            r -= 1
        else:
            t = array[l]
            array[l] = array[r - 1]
            array[r - 1] = t

            l += 1
            r -= 1

    return r


def split2(array, b):
    l = 0
    m = 0
    r = len(array)

    while m != r:
        if array[m] == b:
            m += 1
        elif array[m] > b:
            c = array[m]
            array[m] = array[r - 1]
            array[r - 1] = c

            r -= 1
        else:
            c = array[m]
            array[m] = array[l]
            array[l] = c

            l += 1
            m += 1

    return array, r


def find_median(array):
    n = len(array)
    med = math.ceil(n / 2)

    while len(array) > 1:
        n = len(array)
        m = random.randint(0, n)
        b = array[m]

        i = 0
        k = n

        while i != k:
            if array[i] <= b:
                i += 1
            elif array[k - 1] > b:
                k -= 1
            else:
                t = array[k - 1]
                array[k - 1] = array[i]
                array[i] = t

                i += 1
                k -= 1

        if i < med:
            array = array[i:]
            med -= i
        elif i > med:
            array = array[:i]
        else:
            return b


def partition(array, l, p):
    if l == p:
        return l

    x = array[p - 1]
    i = l - 1
    j = l

    while j < p:
        if array[j - 1] <= x:
            t = array[i]
            array[i] = array[j - 1]
            array[j - 1] = t

            i += 1

        j += 1

    t = array[i]
    array[i] = array[p - 1]
    array[p - 1] = t

    i += 1

    return i


def quick_sort(array, l, p):
    if l > p:
        return

    x = partition(array, l, p)
    quick_sort(array, l, x - 1)
    quick_sort(array, x + 1, p)


def merge(A, B):
    e = []

    n = len(A)
    m = len(B)

    if n == 0:
        return B
    if m == 0:
        return A

    A.append(sys.maxsize)
    B.append(sys.maxsize)

    i = 1
    j = 1
    k = 1

    while k <= (n + m):
        if A[i-1] <= B[j-1]:
            e.append(A[i-1])
            i += 1
        else:
            e.append(B[j-1])
            j += 1

        k += 1

    return e


def merge_sort(array):
    n = len(array)
    if n > 1:
        middle = math.floor(n/2)
        return merge(merge_sort(array[:middle]), merge_sort(array[middle:]))
    else:
        return array

