# Ряд - 2


def row_2(a, b):
    if a < b:
        for num in range(a, b + 1):
            print(num, end=' ')
    else:
        for num in range(a, b - 1, -1):
            print(num, end=' ')


a, b = int(input()), int(input())
row_2(a, b)
