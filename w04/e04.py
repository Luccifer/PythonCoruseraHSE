# Принадлежит ли точка квадрату - 1


def is_point_in_square(x, y):
    axis_x = -1 <= x <= 1
    axis_y = -1 <= y <= 1
    return axis_x and axis_y


if __name__ == '__main__':
    x, y = float(input()), float(input())
    if is_point_in_square(x, y):
        print("YES")
    else:
        print("NO")
