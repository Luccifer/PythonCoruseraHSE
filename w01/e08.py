# Вторая справа цифра

num = int(input())


def second_figure(num):
    if num < 10:
        ans = 0
    elif num >= 100:
        ans = (num // 10) % 10
    else:
        ans = num // 10
    return print(ans)


second_figure(num)
