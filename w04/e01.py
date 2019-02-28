# Минимум 4 чисел


def min4(a, b, c, d):
    return min(min(a, b), min(c, d))


if __name__ == '__main__':
    a, b, c, d = int(input()), int(input()), int(input()), int(input())
    print(min4(a, b, c, d))
