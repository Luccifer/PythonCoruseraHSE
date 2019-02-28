# Количество слов в тексте

import sys

print(len(set(sys.stdin.read().split())))
# print(len(set(map(str.strip, sys.stdin.read().split()))))
