# Наименьший положительный


def least_positive(nums):
    max_n = max(nums)
    min_n = 1
    for num in nums:
        if 1 <= num <= max_n:
            min_n, max_n = num, num
    print(min_n)


nums = list(map(int, input().split()))
least_positive(nums)
