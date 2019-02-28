# Максимальное число подряд идущих равных


def max_number_of_equal(num):
    prev_num = num
    num_equal = 1
    max_num_equal = 0
    while num != 0:
        num = int(input())
        if num == prev_num:
            num_equal += 1
            continue
        if num_equal > max_num_equal:
            max_num_equal = num_equal
        prev_num = num
        num_equal = 1
    return max_num_equal


# for the test
def max_number_of_equal_t(*args):
    num = args[0]
    prev_num = num
    num_equal = 1
    max_num_equal = 0
    i = 1
    while num != 0:
        num = args[i]
        i += 1
        if num == prev_num:
            num_equal += 1
            continue
        if num_equal > max_num_equal:
            max_num_equal = num_equal
        prev_num = num
        num_equal = 1
    return max_num_equal


if __name__ == '__main__':
    num = int(input())
    print(max_number_of_equal(num))
