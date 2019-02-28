# Мороженое


def ice_cream(k):
    nums = {1, 2, 4, 7}
    if k in nums:
        return 'NO'
    return 'YES'


if __name__ == '__main__':
    k = int(input())
    print(ice_cream(k))
