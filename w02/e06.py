# Квартиры


def flats(x, y):
    z = (y - x) + 1
    con = y % z == 0

    if con:
        ans = "YES"
    else:
        ans = "NO"
    return ans


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    print(flats(x, y))
