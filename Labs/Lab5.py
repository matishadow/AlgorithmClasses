def to_dec(number):
    result = 0

    for b in number:
        result = (result << 1) + int(b)

    return result
