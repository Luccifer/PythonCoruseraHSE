# Лесенка


def ladder(n):
    nums = (1, 2, 3, 4, 5, 6, 7, 8, 9)
    for step in range(n):
        for num in nums[:step + 1]:
            print(num, end='')
        print()


n = int(input())
ladder(n)
