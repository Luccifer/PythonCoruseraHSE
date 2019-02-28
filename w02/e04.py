# Високосный год


def leap_year(num):
    con1 = num % 4 == 0
    con2 = num % 100 != 0
    con3 = num % 400 == 0

    if (con1 and con2) or con3:
        ans = "YES"
    else:
        ans = "NO"
    return ans


if __name__ == '__main__':
    num = int(input())
    print(leap_year(num))
