# Возведение в степень


def power(a, n):
    # if n == 0:
    #     return 1
    # if n != 0:
    #     n -= 1
    #     power(a, n)
    # return a * (a ** n)
    if n != 0:
        n -= 1
        power(a, n)
        return a * (a ** n)
    return 1


if __name__ == '__main__':
    a = float(input())
    n = int(input())
    print(power(a, n))
