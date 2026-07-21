#Repeated number triangle

print('Repeated number triangle')
n = 5
for i in range(1, n + 1):
    for  j in range(1, i + 1):
        print(i, end = "")

    print("")
#-----------------------------------
#Increasing number triangle

print('Increasing number triangle')
n = 5
for i in range(1, n + 1):
    for  j in range(1, i + 1):
        print("{}".format(j), end = "")

    print("")

#------------------------------------
#Number triangle with stars

print('Number triangle with stars')
n = 5
for i in range(1, n + 1):
    for  j in range(1, i + 1):
        print("{}".format(j), end = "")

    print("*")

#-----------------------------------
#Diamond Number Pattern

print("Diamond Number Pattern")
n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print("{}".format(j), end = " ")

    print("")
for i in range(n, -1, -1):
    for j in range(1, i):
        print("{}".format(j), end = " ")

    print("")

#------------------------------------
#Diamond

print('Diamond')
n = 5
for i in range(1, n + 1):

    for j in range(n - i):
        print(" ", end = "")

    for j in range(2*i - 1):
        print("*", end = "")

    print("")

for i in range(n - 1, -1, -1):

    for j in range(n - i):
        print(" ", end = "")

    for j in range(2*i - 1):
        print("*", end = "")


    print("")

#-----------------------------------
#Right Aligned Half Pyramid

print("Right Aligned Half Pyramid")
n = 5
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end = "")

    for j in range(i):
        print("*", end = "")
        

    print("")

#-----------------------------------
#Pyramid

print('Pyramid')
n = 5
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end = "")

    for j in range(2*i - 1):
        print("*", end = "")
        

    print("")

#-----------------------------------
#Pyramid
print('Pyramid')
n = 5
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))

#------------------------------------
#Square

print('Square')
n = 5
for _ in range(n):
    print("*" * n)

#------------------------------------
#Hollow Square

print('Hollow Square')
n = 5
for i in range(n):
    if i != 0 and i != n - 1:
        print("*" + " " * (n - 2) + "*")
    else:
        print("*" * n)
    
#------------------------------------
#Left Half Pyramid

print('Left Half Pyramid')
n = 5
for i in range(1, n + 1):
    print("*" * i)
               
#------------------------------------
#Inverted Left Half Pyramid

print('Inverted Left Half Pyramid')
n = 5
for i in range(n, 0, -1):
    print("*" * i)

#------------------------------------
#Right Half Pyramid

print('Right Half Pyramid')
n = 5
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * i)
    
#------------------------------------
# Inverted Right Half Pyramid

print('Inverted Right Half Pyramid')
n = 5
for i in range(n, 0, -1):
    print(" " * (n - i) + "*" * i)

#------------------------------------
# Continuous Numbers

print('Continuous Numbers')
n = 5
j = 1
for i in range(1, n + 1):
    for _ in range(i):
        print(j, end = "")
        j += 1
    print()
  
#------------------------------------
# Reverse Triangle with numbers

print('Reverse Triangle with numbers')
n = 5

for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(j, end = "")
    print()

#------------------------------------
# Reverse Repeated Numbers

print('Reverse Repeated Numbers')
n = 5

for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(i, end = "")
    print()

#------------------------------------
# Full Pyramid
    
print('Full Pyramid')
n = 5

for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end = "")

    for j in range(2 * i - 1):
        print("*", end = "")
    print()

#------------------------------------
# Inverted Pyramid
    
print('Inverted Pyramid')
n = 5

for i in range(n, 0, -1):
    for j in range(n - i):
        print(" ", end = "")

    for j in range(2 * i - 1, 0, -1):
        print("*", end = "")
    print()

#------------------------------------
# Hollow Pyramid
    
print('Hollow Pyramid')
n = 5

for i in range(1, n):
    for j in range(n - i):
        print(" ", end = "")

    if i == 1:
        print("*")
    else:
        print("*" + " " * (2 * i - 3) + "*")
    
print("*" * (2 * n - 1))

#------------------------------------
# Number Pyramid
    
print('Number Pyramid')
n = 5

for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end = "")

    for j in range(2 * i - 1):
        print(i, end = "")

    print()

#------------------------------------
# Hourglass
    
print('Hourglass')
n = 5

for i in range(n, 0, -1):
    for j in range(n - i):
        print(" ", end = "")

    for j in range(2 * i - 1, 0, -1):
        print("*", end = "")
    print()

for i in range(2, n + 1):
    for j in range(n - i):
        print(" ", end = "")

    for j in range(2 * i - 1):
        print("*", end = "")
    print()

#------------------------------------
# X Pattern
    
print('X Pattern')
n = 5

for i in range(n, 0, -1):
    for j in range(n - i):
        print(" ", end = "")
    if i == 1:
        print("*")
    else:
        print("*" + " " * (2 * i - 3) + "*")

for i in range(2, n + 1):
    for j in range(n - i):
        print(" ", end = "")

    print("*" + " " * (2 * i - 3) + "*")
