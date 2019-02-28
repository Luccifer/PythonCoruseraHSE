# Самое частое слово

from collections import Counter


def most_frequent_word(f_in):
    words = f_in.read().split()
    count = Counter(words)
    if len(count.most_common()) == 1:
        return count.most_common()[0][0]
    if count.most_common(1)[0][1] == 1:
        return sorted(words)[0]
    if count.most_common(2)[0][1] == count.most_common(2)[1][1]:
        return sorted(count.most_common(2))[0][0]
    return count.most_common(1)[0][0]


if __name__ == '__main__':
    f_in = open("input.txt", "r", encoding="utf8")
    print(most_frequent_word(f_in), end='')
    f_in.close()
