# Встречалось ли число раньше


def number_before(input_list):
    numbers = set()
    for num in input_list:
        if num in numbers:
            print('YES')
        else:
            print('NO')
        numbers.add(num)


input_list = map(int, input().split())
number_before(input_list)
