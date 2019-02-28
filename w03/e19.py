# Переставить два слова


def rearrange(string):
    space = string.find(' ')
    ans = string[space + 1:] + string[space:space + 1] + string[:space]
    return ans


if __name__ == '__main__':
    string = input()
    print(rearrange(string))
