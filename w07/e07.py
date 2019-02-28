# Угадай число


def guess_number(f_in):
    lines = list(map(str.strip, f_in.readlines()))
    n = int(lines[0])
    f_set = set(range(1, n + 1))
    i = 2
    while lines[i] != 'HELP':
        if lines[i] == 'YES':
            f_set.intersection_update(map(int, lines[i - 1].split()))
        elif lines[i] == 'NO':
            f_set.difference_update(map(int, lines[i - 1].split()))
        i += 1
    return sorted(f_set)


if __name__ == '__main__':
    f_in = open("input.txt", "r", encoding="utf8")
    print(*guess_number(f_in))
    f_in.close()
