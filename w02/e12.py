# Шашки


def checkers(col1, row1, col2, row2):
    con1 = (col1 + row1) % 2 == (col2 + row2) % 2
    con2 = (col2 + row2) > (col1 + row1)
    con3 = (col1 >= row1) == (col2 >= row2)

    if con1 and con2 and con3:
        ans = "YES"
    else:
        ans = "NO"
    return ans


if __name__ == '__main__':
    col1 = int(input())
    row1 = int(input())
    col2 = int(input())
    row2 = int(input())
    print(checkers(col1, row1, col2, row2))
