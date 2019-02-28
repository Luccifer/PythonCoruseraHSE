# Количество различных чисел


def quantity_different_numbers(input_list):
    return len(set(input_list))


if __name__ == '__main__':
    input_list = map(int, input().split())
    print(quantity_different_numbers(input_list))
