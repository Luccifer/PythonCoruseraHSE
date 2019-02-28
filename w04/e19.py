# Сумма последовательности


def sum_of_sequence(n):
    m = n
    if m != 0:
        m = int(input())
        return n + sum_of_sequence(m)
    return n


if __name__ == '__main__':
    n = int(input())
    print(sum_of_sequence(n))
