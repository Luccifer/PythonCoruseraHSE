# Цвет клеток шахматной доски


def cell_comparison(col1, row1, col2, row2):
    con1 = (col1 + row1) % 2 == 0 and (col2 + row2) % 2 == 0
    con2 = (col1 + row1) % 2 != 0 and (col2 + row2) % 2 != 0

    if con1 or con2:
        ans = "YES"
    else:
        ans = "NO"
    return ans


if __name__ == '__main__':
    col1 = int(input())
    row1 = int(input())
    col2 = int(input())
    row2 = int(input())
    print(cell_comparison(col1, row1, col2, row2))
