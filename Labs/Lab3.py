import math


def euclid_rec(a, b):
    if b == 0:
        return a

    return euclid_rec(b, a % b)


def euclid_itr(a, b):
    while b != 0:
        c = a % b
        a = b
        b = c

    return a


def extended_euclid_rec(a, b):
    if b == 0:
        return 1, 0, a

    xp, yp, d = extended_euclid_rec(b, a % b)
    c = math.floor(a / b)

    return yp, xp - c * yp, d


def extended_euclid_itr(a, b):
    x = 0
    old_x = 1

    y = 1
    old_y = 0

    d = b
    old_d = a

    while d != 0:
        quotient = old_d // d
        (old_d, d) = (d, old_d - quotient * d)
        (old_x, x) = (x, old_x - quotient * x)
        (old_y, y) = (y, old_y - quotient * y)

    return old_x, old_y, old_d


def are_co_prime(x, y):
    return euclid_itr(x, y) == 1


def modular_multiplicative_inverse(a, mod):
    if not are_co_prime(a, mod):
        return None

    if a > mod:
        a %= mod

    x, y, d = extended_euclid_rec(a, mod)

    return x % mod


