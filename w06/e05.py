# Создание архива


def archive_creation(s):
    f, n = s[0], s[1]
    b = []
    i = 0
    while i < n:
        a = int(input())
        b.append(a)
        i += 1
    b.sort()
    j = 0
    p = 0
    while j + 1 <= n:
        f -= b[j]
        j += 1
        if f < 0:
            break
        p += 1
        if f == 0:
            p = n
    return p


if __name__ == '__main__':
    s = list(map(int, input().split()))
    print(archive_creation(s))
