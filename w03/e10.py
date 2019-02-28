# Квадратное уравнение - 1


def quadratic_equation_1(a, b, c):
    d = b**2 - (4 * a * c)
    if d == 0 and a != 0:
        x = (- b / (2 * a))
        ans = (round(x, 2), )
    elif d > 0:
        x1 = round((- b - d**0.5) / (2 * a), 6)
        x2 = round((- b + d**0.5) / (2 * a), 5)
        ans = (x2, x1) if x1 > x2 else (x1, x2)
    else:
        ans = ""
    return ans


if __name__ == '__main__':
    a = float(input())
    b = float(input())
    c = float(input())
    print(*quadratic_equation_1(a, b, c))
