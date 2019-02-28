# Наименьший нечетный


def least_odd(nums):
    min_odd = 0
    i = 0
    for num in nums:
        if num % 2 != 0:
            if i == 0:
                min_odd = num
                i += 1
            elif num < min_odd:
                min_odd = num
    print(min_odd)
    # print(min([i for i in nums if i % 2 != 0]))


nums = list(map(int, input().split()))
least_odd(nums)
