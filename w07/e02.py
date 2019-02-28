# Количество совпадающих


def quantity_matching_numbers(input_list_1, input_list_2):
    return len(set(input_list_1) & set(input_list_2))


if __name__ == '__main__':
    input_list_1 = map(int, input().split())
    input_list_2 = map(int, input().split())
    print(quantity_matching_numbers(input_list_1, input_list_2))
