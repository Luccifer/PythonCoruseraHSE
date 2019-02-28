# Упорядочить три числа


def sort_num(a, b, c):
    con1 = a >= b and b >= c
    con2 = b >= a and a >= c
    con3 = c >= a and a >= b
    con4 = b < a > c and b < c
    con5 = a < b > c and a < c

    if con1:
        a, b, c = c, b, a
    elif con2:
        a, b, c = c, a, b
    elif con3:
        a, b, c = b, a, c
    elif con4:
        a, b, c = b, c, a
    elif con5:
        a, b, c = a, c, b
    return a, b, c


if __name__ == '__main__':
    a, b, c = int(input()), int(input()), int(input())
    print(*sort_num(a, b, c))
