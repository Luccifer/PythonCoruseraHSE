# Сумма ряда


def sum_of_series(num):
    i = 1
    sum = 1
    while i < num:
        i += 1
        sum += 1 / i**2
    return round(sum, 5)


if __name__ == '__main__':
    num = int(input())
    print(sum_of_series(num))
