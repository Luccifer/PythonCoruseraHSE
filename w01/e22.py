# Симметричное число*

num = int(input())

symmetry1 = (num // 10**3) == (num % 10)
symmetry2 = (num // 10**2 % 10) == (num // 10**1 % 10)

print(1 if symmetry1 and symmetry2 else 0)
