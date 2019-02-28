# Принадлежит ли точка кругу


def is_point_in_circle(x, y, xc, yc, r):
    axis_x = (x - xc) ** 2
    axis_y = (y - yc) ** 2
    if (axis_x + axis_y)**0.5 <= r:
        return "YES"
    return "NO"


if __name__ == '__main__':
    x, y = float(input()), float(input())
    xc, yc, r = float(input()), float(input()), float(input())
    print(is_point_in_circle(x, y, xc, yc, r))
