# Цена товара


def price(num):
    rubs = int(num)
    kops = round((num - rubs) * 100)
    return rubs, kops


if __name__ == '__main__':
    num = float(input())
    print(*price(num))
