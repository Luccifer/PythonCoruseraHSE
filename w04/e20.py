# Разворот последовательности


def reversal_sequence(n):
    m = n
    if m != 0:
        m = int(input())
        reversal_sequence(m)
        return print(n)
    return print(m)


if __name__ == '__main__':
    n = int(input())
    reversal_sequence(n)
