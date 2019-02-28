# Спички*

import math


def matches(n):
    # https://oeis.org/A078633
    return (2 * n) + math.ceil(2 * math.sqrt(n))


if __name__ == '__main__':
    n = int(input())
    print(matches(n))
