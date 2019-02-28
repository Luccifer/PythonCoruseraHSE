# Количество положительных


def number_of_positive(nums):
    i = 0
    for num in nums:
        if num > 0:
            i += 1
    print(i)


nums = list(map(int, input().split()))
number_of_positive(nums)
