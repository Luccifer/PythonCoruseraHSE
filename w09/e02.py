# Добавить, умножить

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

    def __add__(self, other):
        added_matrix = [list(map(sum, zip(*temp)))
                        for temp in zip(self.lists, other.lists)]
        return Matrix(added_matrix)

    def __mul__(self, other):
        mul_matrix = deepcopy(self.lists)
        for i in range(len(mul_matrix)):
            mul_matrix[i] = list(map(lambda x: x * other, mul_matrix[i]))
        return Matrix(mul_matrix)

    __rmul__ = __mul__

    def size(self):
        return len(self.lists), len(self.lists[0])


if __name__ == '__main__':
    exec(stdin.read())
