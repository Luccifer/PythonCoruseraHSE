# Четные элементы


def even_elements(nums):
    for num in nums:
        if num % 2 == 0:
            print(num, end=' ')


nums = list(map(int, input().split()))
even_elements(nums)
