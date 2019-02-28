# Замена подстроки


def replacing_substring(string):
    if string.count('1'):
        string = string.replace('1', 'one')
    return string


if __name__ == '__main__':
    string = input()
    print(replacing_substring(string))
