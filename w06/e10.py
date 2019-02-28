# Сортировка подсчетом


def sorting_by_counting(a):
    c = [0] * 101
    for i in a:
        c[i] += 1
    b = 0
    for j in range(101):
        for k in range(c[j]):
            a[b] = j
            b += 1
    return a


if __name__ == '__main__':
    input_list = list(map(int, input().split()))
    print(*sorting_by_counting(input_list))
