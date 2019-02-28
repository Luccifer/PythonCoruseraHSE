# Улитка*

h = int(input())
a = int(input())
b = int(input())

days = 1

while h > a:
    h += b
    days += 1
    h -= a

print(days)
