# Округление по российским правилам

from math import ceil


def rounding_off(num):
    tenths = ((num * 10) % 10) / 10
    if tenths >= 0.5:
        num_round = ceil(num)
    else:
        num_round = int(num)
    return num_round


if __name__ == '__main__':
    num = float(input())
    print(rounding_off(num))
