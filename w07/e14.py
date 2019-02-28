# Номер появления слова


def word_occurrence_number(f_in):
    words = list(map(str.strip, f_in.read().split()))
    count = {}
    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 0
        print(count[word], end=' ')


f_in = open("input.txt", "r", encoding="utf8")
word_occurrence_number(f_in)
f_in.close()
