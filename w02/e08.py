# Шоколадка


def getting_pieces(n, m, k):
    con1 = k % n == 0
    con2 = k % m == 0
    con3 = k <= (n * m)

    if (con1 or con2) and con3:
        ans = "YES"
    else:
        ans = "NO"
    return ans


if __name__ == '__main__':
    n = int(input())
    m = int(input())
    k = int(input())
    print(getting_pieces(n, m, k))
