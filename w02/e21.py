# Сложное уравнение*


def complex_equation(a, b, c, d):
    if a == b == 0:
        return "INF"
    if a == 0 or b % a != 0 or (c * (-b // a)) + d == 0:
        return "NO"
    return -b // a


if __name__ == '__main__':
    # a, b, c, d = int(input()), int(input()), int(input()), int(input())
    a, b, c, d = [int(input()) for _ in range(4)]
    print(complex_equation(a, b, c, d))
