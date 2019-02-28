# Площадь треугольника


def area_of_triangle(a, b, c):
    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    return round(s, 6)


if __name__ == '__main__':
    a = float(input())
    b = float(input())
    c = float(input())
    print(area_of_triangle(a, b, c))
