# Кубики


def cubes(f_in):
    lines = f_in.readlines()
    i = list(map(int, lines[0].split()))
    colors_1 = set(map(int, lines[1:i[0] + 1]))
    colors_2 = set(map(int, lines[i[0] + 1:sum(i) + 1]))
    print(len(colors_1 & colors_2))
    print(*sorted(colors_1 & colors_2))
    print(len(colors_1 - colors_2))
    print(*sorted(colors_1 - colors_2))
    print(len(colors_2 - colors_1))
    print(*sorted(colors_2 - colors_1))


f_in = open("input.txt", "r", encoding="utf8")
cubes(f_in)
f_in.close()
