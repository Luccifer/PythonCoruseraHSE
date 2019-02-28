# Список квадратов


def list_of_squares(num):
    i = 1
    squares = []
    while i**2 <= num:
        squares.append(i**2)
        i += 1
    return squares


if __name__ == '__main__':
    num = int(input())
    print(*list_of_squares(num))
