# Сложение без сложения


def sum(a, b):
    if b != 0:
        b -= 1
        a += 1
        return sum(a, b)
    return a


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(sum(a, b))
