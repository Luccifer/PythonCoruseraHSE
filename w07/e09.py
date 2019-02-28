# Полиглоты


def polyglots(f_in):
    lines = list(map(str.strip, f_in.readlines()))
    n = int(lines[0])
    set_1, set_2, set_3 = set(), set(), set()
    k = 2
    j = 0
    s = len(lines[1:])
    while j < n:
        line = lines[k]
        if line.isalpha():
            set_1.add(line)
            set_3.update(set_1)
            if s > k:
                k += 1
                continue
        elif j == 0:
            set_2.update(set_1)
        set_2.intersection_update(set_1)
        set_1.clear()
        j += 1
        if s > k:
            k += 1
    print(len(set_2), *set_2, sep='\n')
    print(len(set_3), *set_3, sep='\n')


f_in = open("input.txt", "r", encoding="utf8")
polyglots(f_in)
f_in.close()
