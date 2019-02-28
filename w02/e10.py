# Знак числа


def sign(x):
    if x > 0:
        n = 1
    elif x < 0:
        n = -1
    else:
        n = 0
    return n


if __name__ == '__main__':
    x = int(input())
    print(sign(x))
