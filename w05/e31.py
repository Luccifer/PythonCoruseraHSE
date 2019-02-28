# Переставить соседние


def rearrange_neighboring(nums):
    i = 0
    nums_rn = []
    while i < len(nums) - 1:
        nums_rn.append(nums[i + 1])
        nums_rn.append(nums[i])
        i += 2
    if len(nums) % 2 != 0:
        nums_rn.append(nums[-1])
    return nums_rn


if __name__ == '__main__':
    nums = list(map(int, input().split()))
    print(*rearrange_neighboring(nums))
