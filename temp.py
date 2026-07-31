n = int(input('enter the no: '))
m = int(input('enter how many time the no should be printed: '))

b = n
for _ in range(1, m):
    b = b * 10
    n = n + b

print(n)