# Последний максимум


def last_high(nums):
    i = 0
    max_i = i
    max_n = nums[0]
    for num in nums:
        if num >= max_n:
            max_n, max_i = num, i
        i += 1
    print(max_n, max_i)


nums = list(map(int, input().split()))
last_high(nums)
