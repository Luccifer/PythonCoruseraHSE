# Утренняя пробежка


def morning_running(x, y):
    days = 1
    while x < y:
        x += x * 0.1
        days += 1
    return days


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    print(morning_running(x, y))
