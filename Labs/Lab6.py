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
            array[m] = array[r-1]
            array[r - 1] = c

            r -= 1
        else:
            c = array[m]
            array[m] = array[l]
            array[l] = c

            l += 1
            m += 1

    return array, r

