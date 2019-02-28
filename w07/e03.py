# Пересечение множеств


def intersection_of_many(input_list_1, input_list_2):
    return sorted(set(input_list_1) & set(input_list_2))


if __name__ == '__main__':
    input_list_1 = map(int, input().split())
    input_list_2 = map(int, input().split())
    print(*intersection_of_many(input_list_1, input_list_2))
