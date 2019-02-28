# Сумма квадратов


def sum_of_squares(num):
    sum_sqr = 0
    i = 0
    while num > i:
        i += 1
        sum_sqr += i**2
    return sum_sqr


if __name__ == '__main__':
    num = int(input())
    print(sum_of_squares(num))
