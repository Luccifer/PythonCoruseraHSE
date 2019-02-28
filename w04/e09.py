# Минимальный делитель числа


def min_divisor(num):
    divisor = 2
    sqrt_num = int(num**0.5) + 1
    while num % divisor:
        if divisor == sqrt_num:
            return num
        divisor += 1
    return divisor


if __name__ == '__main__':
    num = int(input())
    print(min_divisor(num))
