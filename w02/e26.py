# Минимальный делитель


def least_divisor(num):
    i = 2
    while num % i != 0:
        i += 1
    return i


if __name__ == '__main__':
    num = int(input())
    print(least_divisor(num))
