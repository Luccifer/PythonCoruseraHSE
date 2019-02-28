# Проценты


def percentages(p, x, y):
    p /= 100
    kop = (round((((x * p) * 10) % 10) * 10) + y + int(y * p))
    rub = int((x * p)) + x + (kop // 100)
    return rub, kop % 100


if __name__ == '__main__':
    p = int(input())
    x = int(input())
    y = int(input())
    print(*percentages(p, x, y))
