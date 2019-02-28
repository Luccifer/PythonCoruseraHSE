# Флаги


def flags(n):
    flag = ("+___", 0, "|__\\", "|   ")
    for part in flag:
        for i in range(1, n + 1):
            if part == 0:
                print("|%s /" % i, end=' ')
            else:
                print(part, end=' ')
        print()


n = int(input())
flags(n)
