import math
import cmath


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
