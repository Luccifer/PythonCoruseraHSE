# Первое и последнее вхождение


def first_last_occurrence_f(string):
    first_f = string.find('f')
    last_f = len(string) - string[::-1].find('f') - 1
    if first_f == -1:
        ans = ""
    elif last_f > first_f:
        ans = (first_f, last_f)
    else:
        ans = (first_f, )
    return ans


if __name__ == '__main__':
    string = input()
    print(*first_last_occurrence_f(string))
