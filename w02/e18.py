# Коробки


def comparison_of_boxes(a1, b1, c1, a2, b2, c2):
    box1 = sorted((a1, b1, c1))
    box2 = sorted((a2, b2, c2))
    if box1 == box2:
        ans = 'Boxes are equal'
    elif box1[0] >= box2[0] and box1[1] >= box2[1] and box1[2] >= box2[2]:
        ans = 'The first box is larger than the second one'
    elif box1[0] <= box2[0] and box1[1] <= box2[1] and box1[2] <= box2[2]:
        ans = 'The first box is smaller than the second one'
    else:
        ans = 'Boxes are incomparable'
    return ans


if __name__ == '__main__':
    a1, b1, c1 = int(input()), int(input()), int(input())
    a2, b2, c2 = int(input()), int(input()), int(input())
    print(comparison_of_boxes(a1, b1, c1, a2, b2, c2))
