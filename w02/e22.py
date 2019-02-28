# Котлеты*


def cutlets(k, m, n):
    # if n < k:
    #     return 2 * m
    # if 2 * n % k != 0:
    #     return (2 * n // k * m) + m
    # return 2 * n // k * m
    return m * max(2, ((n * 2 + (k - 1)) // k))


if __name__ == '__main__':
    k, m, n = [int(input()) for _ in range(3)]
    print(cutlets(k, m, n))
