# Максимум из двух


def maximum_of_two(a, b):
    if a > b:
        ans = a
    else:
        ans = b
    return ans


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(maximum_of_two(a, b))
