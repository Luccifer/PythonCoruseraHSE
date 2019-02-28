# Ряд - 1


def row_1(a, b):
    for num in range(a, b + 1):
        print(num, end=' ')


a, b = int(input()), int(input())
row_1(a, b)
