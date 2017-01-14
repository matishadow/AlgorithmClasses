import math
import cmath
import Labs.Lab2


def digits(k, n):
    binary_number = [0] * n

    is_positive = True
    if k < 0:
        is_positive = False
        k *= -1

    i = n - 1
    while k != 0:
        binary_number[i] = k % 2
        k //= 2
        i -= 1

    if not is_positive:
        for i in range(n):
            binary_number[i] = 1 - binary_number[i]
        number_to_add = [0] * n
        number_to_add[n - 1] = 1
        binary_number = Labs.Lab2.add(number_to_add, binary_number)

    return binary_number


def rec_fft(array):
    n = len(array)
    if n == 1:
        return array

    omega_n = cmath.exp((2 * math.pi * 1j) / n)

    omega = 1

    a0 = []
    a1 = []

    for i in range(n):
        if i % 2 == 0:
            a0.append(array[i])
        else:
            a1.append(array[i])

    y0 = rec_fft(a0)
    y1 = rec_fft(a1)

    y = [0] * n
    for k in range(0, n // 2):
        y[k] = y0[k] + omega * y1[k]
        y[k + (n // 2)] = y0[k] - omega * y1[k]

        omega *= omega_n

    return y
