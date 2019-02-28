# Количество слов в тексте

import sys


def number_of_words():
    words = []
    for line in sys.stdin.readlines():
        words.extend(line.split())
    print(len(set(words)))


number_of_words()
