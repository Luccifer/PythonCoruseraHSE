# Отсортировать список участников по алфавиту


def sort_list(fin, fout):
    temp = []
    for line in fin.readlines():
        temp.append(' '.join(line.split()[:2] + line.split()[3:]))
    temp.sort()
    print('\n'.join(temp), file=fout)


fin = open('input.txt', 'r', encoding='utf8')
fout = open('output.txt', 'w', encoding='utf8')
sort_list(fin, fout)
fin.close()
fout.close()
