n = 5
for i in range(1, n):
    for j in range(n - i):
        print(" ", end = "")

    if i == 1:
        print("*")
    else:    
        print("*" + " " * (2 * i - 3) + "*")

print("*" * (2 * n - 1))