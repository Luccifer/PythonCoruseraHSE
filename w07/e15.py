# Словарь синонимов


def synonym_dictionary(f_in):
    n = int(f_in.readline())
    synonym = {}
    for i in range(n):
        temp = list(map(str.strip, f_in.readline().split()))
        synonym[temp[0]] = temp[1]
    ans = f_in.readline().strip()
    for el in synonym:
        if ans == el:
            print(synonym[el])
        elif ans == synonym[el]:
            print(el)


f_in = open("input.txt", "r", encoding="utf8")
synonym_dictionary(f_in)
f_in.close()
