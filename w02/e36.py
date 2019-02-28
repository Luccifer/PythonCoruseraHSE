# Количество четных элементов последовательности


def number_of_even(num):
    even = 0
    while num != 0:
        if num % 2 == 0:
            even += 1
        num = int(input())
    return even


# for the test
def number_of_even_t(*args):
    num = args[0]
    even = 0
    i = 1
    while num != 0:
        if num % 2 == 0:
            even += 1
        num = args[i]
        i += 1
    return even


if __name__ == '__main__':
    num = int(input())
    print(number_of_even(num))
