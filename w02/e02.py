# Какое число больше?


def greater_number(num1, num2):
    if num1 > num2:
        ans = 1
    elif num2 > num1:
        ans = 2
    else:
        ans = 0
    return ans


if __name__ == '__main__':
    num1 = int(input())
    num2 = int(input())
    print(greater_number(num1, num2))
