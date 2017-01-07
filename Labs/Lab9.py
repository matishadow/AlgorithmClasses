import math
import cmath


def bit_reverse_copy(array):
    n = len(array)
    result_array = [0] * n

    for i in range(n):
        number = bin(i)[2:]
        number = ('0' * (int(math.log(n, 2)) - len(number))) + number
        result_array[i] = array[int(number[::-1], 2)]

    return result_array


def iter_fft(array):
    array = bit_reverse_copy(array)

    n = len(array)
    for s in range(1, int(math.log(n, 2)) + 1):
        m = 2 ** s
        omega_m = cmath.exp((2 * math.pi * 1j) / m)
        omega = 1

        for j in range(0, m // 2):
            for k in range(j, n, m):
                t = omega * array[k + m // 2]
                u = array[k]
                array[k] = u + t
                array[k + m // 2] = u - t

            omega = omega * omega_m

    return array
