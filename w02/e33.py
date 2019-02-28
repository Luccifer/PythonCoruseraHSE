# Длина последовательности


def sequence_length(num):
    len_num = 0
    while num != 0:
        len_num += 1
        num = int(input())
    return len_num


# for the test
def sequence_length_t(*args):
    num = args[0]
    len_num = 0
    i = 1
    while num != 0:
        len_num += 1
        num = args[i]
        i += 1
    return len_num


if __name__ == '__main__':
    num = int(input())
    print(sequence_length(num))
