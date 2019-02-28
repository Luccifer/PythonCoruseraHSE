# Максимум трех чисел


def maximum_of_three(num1, num2, num3):
    if num3 <= num1 >= num2:
        ans = num1
    elif num2 >= num3:
        ans = num2
    else:
        ans = num3
    return ans


if __name__ == '__main__':
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    print(maximum_of_three(num1, num2, num3))
