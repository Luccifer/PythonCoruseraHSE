# Сортировка


def sorting(n, a):
    if n == 1:
        return a
    return sorted(a)


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    print(*sorting(n, a))
