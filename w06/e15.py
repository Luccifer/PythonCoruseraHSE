# Проходной балл


def passing_score(f_in):
    lines = f_in.readlines()
    k = int(lines[0])
    a = []
    for line in lines[1:]:
        temp = line.split()
        if int(temp[-1]) >= 40 and int(temp[-2]) >= 40 and int(temp[-3]) >= 40:
            a.append(sum(map(int, temp[:-4:-1])))

    a.sort(reverse=True)
    if len(a) <= k:
        return 0
    elif a[k] == a[0]:
        return 1
    f_k = a.index(a[k])
    return a[f_k - 1]


if __name__ == '__main__':
    f_in = open("input.txt", "r", encoding="utf8")
    f_out = open("output.txt", "w", encoding="utf8")
    print(passing_score(f_in), file=f_out)
    f_in.close()
    f_out.close()
