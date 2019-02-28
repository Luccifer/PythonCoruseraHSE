# Сократите дробь


def gcd(n, m):
    if m != 0:
        return gcd(m, n % m)
    return n


def reduce_fraction(n, m):
    return n // gcd(n, m), m // gcd(n, m)


if __name__ == '__main__':
    n = int(input())
    m = int(input())
    print(*reduce_fraction(n, m))
