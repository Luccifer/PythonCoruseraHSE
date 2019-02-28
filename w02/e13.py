# Тип треугольника


def type_of_triangle(num1, num2, num3):
    if num3 <= num1 >= num2:
        a = num2
        b = num3
        c = num1
    elif num2 >= num3:
        a = num1
        b = num3
        c = num2
    else:
        a = num1
        b = num2
        c = num3
    if c >= a + b:
        ans = 'impossible'
    else:
        sign = a**2 + b**2 - c**2
        if sign > 0:
            ans = 'acute'
        elif sign < 0:
            ans = 'obtuse'
        else:
            ans = 'rectangular'
    return ans


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    c = int(input())
    print(type_of_triangle(a, b, c))
