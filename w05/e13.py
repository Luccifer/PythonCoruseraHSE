# Четные индексы


def even_indices(nums):
    print(*nums[::2])


nums = list(map(int, input().split()))
even_indices(nums)
