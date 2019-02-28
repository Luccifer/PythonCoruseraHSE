# Максимум из двух*

# a = int(input())
# b = int(input())
# c = (a // b) * (b // a)
# print(((a ** (0 ** (b // a))) * (b ** (0 ** (a // b)))) * (a ** c))

num_1 = int(input())
num_2 = int(input())
a = num_1 // num_2
b = num_2 // num_1
c = num_1 ** (a * b)
d = num_1 ** (0 ** b)
f = num_2 ** (0 ** a)
print(c * d * f)
