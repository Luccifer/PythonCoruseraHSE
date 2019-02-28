# Количество элементов, равных максимуму


def number_of_maximum(num):
    max_num = num
    num_max = 1
    while num != 0:
        num = int(input())
        if num == 0:
            continue
        if num > max_num:
            max_num = num
            num_max = 1
        elif num == max_num:
            num_max += 1
    return num_max


# for the test
def number_of_maximum_t(*args):
    num = args[0]
    max_num = num
    num_max = 1
    i = 1
    while num != 0:
        num = args[i]
        i += 1
        if num == 0:
            continue
        if num > max_num:
            max_num = num
            num_max = 1
        elif num == max_num:
            num_max += 1
    return num_max


if __name__ == '__main__':
    num = int(input())
    print(number_of_maximum(num))
