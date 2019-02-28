# Сумма последовательности


def sum_of_the_sequence(num):
    sum_seq = 0
    while num != 0:
        sum_seq += num
        num = int(input())
    return sum_seq


# for the test
def sum_of_the_sequence_t(*args):
    num = args[0]
    sum_seq = 0
    i = 1
    while num != 0:
        sum_seq += num
        num = args[i]
        i += 1
    return sum_seq


if __name__ == '__main__':
    num = int(input())
    print(sum_of_the_sequence(num))
