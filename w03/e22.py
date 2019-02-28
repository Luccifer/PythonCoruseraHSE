# Удаление символа


def deleting_character(string):
    return string.replace('@', '')


if __name__ == '__main__':
    string = input()
    print(deleting_character(string))
