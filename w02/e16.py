# Сколько совпадает чисел


def coincidence_of_numbers(num1, num2, num3):
    if num1 == num2 == num3:
        ans = 3
    elif num1 == num2 or num2 == num3 or num1 == num3:
        ans = 2
    else:
        ans = 0
    return ans


if __name__ == '__main__':
    num1, num2, num3 = int(input()), int(input()), int(input())
    print(coincidence_of_numbers(num1, num2, num3))
