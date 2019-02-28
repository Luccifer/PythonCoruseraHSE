# Коровы


def cows(n):
    if (10 <= n <= 20) or (n % 10 == 0) or (5 <= (n % 10) < 10):
        ans = 'korov'
    elif n % 10 == 1:
        ans = 'korova'
    else:
        ans = 'korovy'
    return ans


if __name__ == '__main__':
    n = int(input())
    print(n, cows(n))
