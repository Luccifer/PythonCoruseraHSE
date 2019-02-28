# Складирование ноутбуков


def storage_of_laptops(a1, b1, c1, a2, b2, c2):
    stock_size = sorted((a1, b1, c1))
    laptop_size = sorted((a2, b2, c2))
    con1 = stock_size[0] < laptop_size[0]
    con2 = stock_size[1] < laptop_size[1]
    con3 = stock_size[2] < laptop_size[2]

    if con1 or con2 or con3:
        quan = 0
    else:
        abc = (a1 // a2) * (b1 // b2) * (c1 // c2)
        acb = (a1 // a2) * (c1 // b2) * (b1 // c2)
        cab = (c1 // a2) * (a1 // b2) * (b1 // c2)
        cba = (c1 // a2) * (b1 // b2) * (a1 // c2)
        bac = (b1 // a2) * (a1 // b2) * (c1 // c2)
        bca = (b1 // a2) * (c1 // b2) * (a1 // c2)
        quan = sorted((abc, acb, cab, cba, bac, bca))[-1]
        # quan = max(abc, acb, cab, cba, bac, bca)
    return quan


if __name__ == '__main__':
    a1, b1, c1 = int(input()), int(input()), int(input())
    a2, b2, c2 = int(input()), int(input()), int(input())
    print(storage_of_laptops(a1, b1, c1, a2, b2, c2))
