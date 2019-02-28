# Координатные четверти


def coordinate_quarters(x1, y1, x2, y2):
    con1 = (x1 > 0) == (x2 > 0)
    con2 = (y1 > 0) == (y2 > 0)

    if con1 and con2:
        ans = "YES"
    else:
        ans = "NO"
    return ans


if __name__ == '__main__':
    x1 = int(input())
    y1 = int(input())
    x2 = int(input())
    y2 = int(input())
    print(coordinate_quarters(x1, y1, x2, y2))
