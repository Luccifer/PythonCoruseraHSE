# Удаление фрагмента


def deletion_of_fragment(string):
    first_h = string.find('h')
    last_h = len(string) - string[::-1].find('h') - 1
    ans = string[:first_h] + string[last_h + 1:]
    return ans


if __name__ == '__main__':
    string = input()
    print(deletion_of_fragment(string))
