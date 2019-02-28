# Четные и нечетные


def even_or_odd(a, b, c):
    con = (a % 2 != 0) == (b % 2 != 0) == (c % 2 != 0)

    if con:
        ans = "NO"
    else:
        ans = "YES"
    return ans


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    c = int(input())
    print(even_or_odd(a, b, c))
