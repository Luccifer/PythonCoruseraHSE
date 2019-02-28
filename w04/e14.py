# Быстрое возведение в степень


def rapid_exp(a, n):
    # if n == 0:
    #     return 1
    # if n % 2 == 0:
    #     return rapid_exp(a * a, n / 2)
    # return a * rapid_exp(a, n - 1)
    if n != 0:
        if n % 2 == 0:
            return rapid_exp(a * a, n / 2)
        return a * rapid_exp(a, n - 1)
    return 1


if __name__ == '__main__':
    a = float(input())
    n = int(input())
    print(rapid_exp(a, n))
