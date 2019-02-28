# Система линейных уравнений - 1


def system_of_linear_equations_1(a, b, c, d, e, f):
    determinant = a*d - c*b
    determinant_x = e*d - f*b
    determinant_y = a*f - c*e
    x = determinant_x / determinant
    y = determinant_y / determinant
    return x, y


if __name__ == '__main__':
    a = float(input())
    b = float(input())
    c = float(input())
    d = float(input())
    e = float(input())
    f = float(input())
    print(*system_of_linear_equations_1(a, b, c, d, e, f))
