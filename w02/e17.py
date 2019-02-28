# Узник замка Иф


def prisoner(a, b, c, d, e):
    brick_size = sorted((a, b, c))
    hole_size = sorted((d, e))
    con1 = brick_size[0] <= hole_size[0]
    con2 = brick_size[1] <= hole_size[1]

    if con1 and con2:
        ans = "YES"
    else:
        ans = "NO"
    return ans


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    print(prisoner(a, b, c, d, e))
