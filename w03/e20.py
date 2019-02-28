# Количество слов


def number_of_words(string):
    return string.count(' ') + 1


if __name__ == '__main__':
    string = input()
    print(number_of_words(string))
