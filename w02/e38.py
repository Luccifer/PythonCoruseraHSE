# Второй максимум


def second_maximum(num):
    max_num = num
    sec_num = 0
    while num != 0:
        num = int(input())
        if num == 0:
            continue
        if sec_num < num < max_num:
            sec_num = num
        elif num >= max_num:
            sec_num = max_num
            max_num = num
    return sec_num


# for the test
def second_maximum_t(*args):
    num = args[0]
    max_num = num
    sec_num = 0
    i = 1
    while num != 0:
        num = args[i]
        i += 1
        if num == 0:
            continue
        if sec_num < num < max_num:
            sec_num = num
        elif num >= max_num:
            sec_num = max_num
            max_num = num
    return sec_num


if __name__ == '__main__':
    num = int(input())
    print(second_maximum(num))
