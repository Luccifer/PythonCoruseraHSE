# Переставить min и max


def rearrange_min_max(nums):
    list_max = max(nums)
    list_min = min(nums)
    index_max = nums.index(list_max)
    index_min = nums.index(list_min)
    nums[index_max] = list_min
    nums[index_min] = list_max
    print(*nums)


nums = list(map(int, input().split()))
rearrange_min_max(nums)
