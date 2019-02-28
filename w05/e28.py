# Ближайшее число


def the_next(n, array, x):
    if array.count(x):
        return x
    if min(array) > x:
        return min(array)
    if max(array) < x:
        return max(array)

    i = 0
    maxs = []
    mins = []
    while i < n:
        if array[i] < x:
            mins.append(array[i])
        else:
            maxs.append(array[i])
        i += 1

    maxs_min = min(maxs)
    if len(maxs) == n:
        return maxs_min
    mins_max = max(mins)
    if len(mins) == n:
        return mins_max

    if (x - mins_max) >= (maxs_min - x):
        return maxs_min
    else:
        return mins_max


if __name__ == '__main__':
    n = int(input())
    array = list(map(int, input().split()))
    x = int(input())
    print(the_next(n, array, x))
