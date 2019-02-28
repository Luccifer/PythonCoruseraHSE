# Частотный анализ

from collections import Counter


def frequency_analysis(f_in):
    words = f_in.read().split()
    count = Counter(words)
    a = list(count.items())
    a.sort(key=lambda x: (-x[1], x[0]))
    for el in a:
        print(el[0])


f_in = open("input.txt", "r", encoding="utf8")
frequency_analysis(f_in)
f_in.close()
