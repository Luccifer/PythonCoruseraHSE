# Выборы Президента

from collections import Counter


def president_elections(f_in, f_out):
    text = f_in.read().split('\n')
    candidates = Counter(text[:-1])
    voices = sum(candidates.values())

    percent = (candidates.most_common(1)[0][1] / voices) * 100
    if percent > 50:
        print(candidates.most_common(1)[0][0], file=f_out)
    else:
        for name, _ in candidates.most_common(2):
            print(name, file=f_out)


f_in = open("input.txt", "r", encoding="utf8")
f_out = open("output.txt", "w", encoding="utf8")
president_elections(f_in, f_out)
f_in.close()
f_out.close()
