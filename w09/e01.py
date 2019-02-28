# Класс

from copy import deepcopy
from sys import stdin


class Matrix:
    def __init__(self, lists):
        self.lists = deepcopy(lists)

    def __str__(self):
        s = []
        for row in self.lists:
            s.append('\t'.join(map(str, row)))
        return '\n'.join(s)

    def size(self):
        return len(self.lists), len(self.lists[0])


if __name__ == '__main__':
    exec(stdin.read())
