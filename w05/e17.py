# Больше предыдущего


def more_than_previous(nums):
    i = 0
    for num in nums[1:]:
        if num > nums[i]:
            print(num, end=' ')
        i += 1


nums = list(map(int, input().split()))
more_than_previous(nums)
