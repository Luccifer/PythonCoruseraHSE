# Слияние списков


def merge(a, b):
    a_len, b_len, ab_len = len(a), len(b), len(a) + len(b)
    c = []
    i, j = 0, 0
    while len(c) < ab_len:
        if a[i] > b[j]:
            if j < b_len - 1:
                c.append(b[j])
                j += 1
            elif i == a_len - 1:
                c.append(b[j])
                c.append(a[i])
                continue
            else:
                c.append(b[j])
                c.extend(a[i:])
                continue
        if a[i] < b[j]:
            if i < a_len - 1:
                c.append(a[i])
                i += 1
            elif j == b_len - 1:
                c.append(a[i])
                c.append(b[j])
                continue
            else:
                c.append(a[i])
                c.extend(b[j:])
                continue
        if a[i] == b[j]:
            if i < a_len - 1:
                c.append(a[i])
                i += 1
            elif j == b_len - 1:
                c.append(a[i])
                c.append(b[j])
                continue
            if j < b_len - 1:
                c.append(b[j])
                j += 1
            elif i == a_len - 1:
                c.append(b[j])
                c.append(a[i])
                continue
    return c


if __name__ == '__main__':
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(*merge(a, b))
