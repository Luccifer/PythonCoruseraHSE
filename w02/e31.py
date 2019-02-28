# Максимум последовательности


def maximum_sequence(num):
    max_num = num
    while num != 0:
        num = int(input())
        if num > max_num:
            max_num = num
    return max_num


# for the test
def maximum_sequence_t(*args):
    num = args[0]
    max_num = num
    i = 1
    while num != 0:
        num = args[i]
        if num > max_num:
            max_num = num
        i += 1
    return max_num


if __name__ == '__main__':
    num = int(input())
    print(maximum_sequence(num))
