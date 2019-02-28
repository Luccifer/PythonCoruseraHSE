# Проверка числа на простоту


def check_for_simplicity(num):
    if num == 2:
        return "YES"
    divisor = 2
    sqrt_num = int(num**0.5) + 1
    while num % divisor:
        if divisor == sqrt_num:
            return "YES"
        divisor += 1
    return "NO"


if __name__ == '__main__':
    num = int(input())
    print(check_for_simplicity(num))
