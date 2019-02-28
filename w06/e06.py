# Гражданская оборона


def civil_defense(n, ni, m, mi):
    if m == 1:
        return list(map(int, ('1 ' * n).split()))

    settlements = []
    for i in range(1, n + 1):
        ni_i = ni[i - 1], i
        settlements.append(ni_i)
    shelters = []
    for j in range(1, m + 1):
        mi_i = mi[j - 1], j
        shelters.append(mi_i)
    settlements.sort()
    shelters.sort()

    dists = []
    k, s = 0, 0
    while len(dists) < n:
        temp1 = (shelters[k][0] - settlements[s][0]) ** 2
        temp2 = (shelters[k + 1][0] - settlements[s][0]) ** 2
        if temp1 <= temp2:
            dists.append((shelters[k][1], settlements[s][1]))
            s += 1
        elif k + 1 < m - 1:
            k += 1
            continue
        else:
            dists.append((shelters[k + 1][1], settlements[s][1]))
            s += 1

    dists.sort(key=lambda el: el[1])
    dists_final = []
    for dist in dists:
        dists_final.append(dist[0])
    return dists_final


if __name__ == '__main__':
    n = int(input())
    ni = list(map(int, input().split()))
    m = int(input())
    mi = list(map(int, input().split()))
    print(*civil_defense(n, ni, m, mi))
