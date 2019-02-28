# Результаты олимпиады


def results_of_olympiad(n):
    a = []
    for i in range(n):
        temp = input().split()
        a.append((temp[0], int(temp[1])))
    a.sort(key=lambda x: x[1], reverse=True)
    for el in a:
        print(el[0])


n = int(input())
results_of_olympiad(n)
