# Делаем срезы


def sections(string):
    ans = (string[2], string[-2], string[:5],
           string[:-2], string[0::2], string[1::2],
           string[::-1], string[::-2], len(string))
    return ans


if __name__ == '__main__':
    string = input()
    print(*sections(string), sep='\n')
