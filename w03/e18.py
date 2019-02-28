# Второе вхождение


def second_occurrence_f(string):
    first_f = string.find('f')
    last_f = len(string) - string[::-1].find('f') - 1
    if first_f == -1:
        ans = -2
    elif last_f > first_f:
        ans = string.find('f', first_f + 1)
    else:
        ans = -1
    return ans


if __name__ == '__main__':
    string = input()
    print(second_occurrence_f(string))
