# Дробная часть


def fraction(num):
    if num < 1:
        frac = num
    else:
        frac = num - int(num)
    return round(frac, 6)


if __name__ == '__main__':
    num = float(input())
    print(fraction(num))
