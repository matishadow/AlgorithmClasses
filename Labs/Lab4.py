import random
import Labs.Lab2
import Labs.Lab3


def is_prime(number, sample_count):
    samples = generate_distinct_random_integers(1, number, sample_count)

    for a in samples:
        if Labs.Lab2.mode_xp(a, number - 1, number) != 1:
            return False

    return True


def generate_distinct_random_integers(a, b, count):
    max_count = b - a

    if a > b or count > max_count:
        return None

    if count == max_count:
        return list(range(a, b))

    random_numbers = []
    step = (b - a) // count

    current_a = a
    current_b = a + step
    for i in range(count):
        random_numbers.append(random.randint(current_a, current_b - 1))

        current_a += step
        current_b += step

    return random_numbers


def generate_prime(min_bits, max_bits, primality_sample):
    while True:
        prime = random.randint(2 ** min_bits, 2 ** max_bits - 1)

        if is_prime(prime, primality_sample):
            break

    return prime


def find_e_d(p, q):
    phi = (p - 1) * (q - 1)

    for i in range(2, phi):
        e = i
        if Labs.Lab3.are_co_prime(e, phi):
            break

    d = Labs.Lab3.modular_multiplicative_inverse(e, phi)

    return e, d


def encrypt(m, n, e):
    return Labs.Lab2.mode_xp(m, e, n)


def decrypt(c, n, d):
    return Labs.Lab2.mode_xp(c, d, n)


def sign(m, n, d):
    return Labs.Lab2.mode_xp(m, d, n)


def verify(s, n, e, m):
    test_m = Labs.Lab2.mode_xp(s, e, n)

    if test_m == m:
        return True
    else:
        return False
