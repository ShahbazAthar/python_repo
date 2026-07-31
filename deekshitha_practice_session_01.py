#print numbers from 1 to 10
i = 1

while i <= 10:
    print(i)
    i += 1

    
#sum of digits
n = int(input("Enter a number: "))
sum = 0

while n > 0:
    digit = n % 10
    sum += digit
    n = n // 10

print( sum)


#reverse a number

n = int(input("Enter a number: "))
reverse = 0

while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10

print( reverse)

#palindrome

n = int(input("Enter a number: "))
temp = n
reverse = 0

while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp = temp // 10

if n == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")

#count of digits
n = int(input("Enter a number: "))
count = 0

while n > 0:
    count += 1
    n = n // 10

print(count)


#finonacci series
n = int(input("Enter number"))

a = 0
b = 1
count = 0

while count < n:
    print(a)
    c = a + b
    a = b
    b = c
    count += 1

#print all odd numbers  1 to 50

for i in range(1, 51, 2):
    print(i)

#largest numbers

numbers = [15, 8, 25, 10, 30]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest =", largest)

#count vowels 
text = input("Enter a string: ")
count = 0

for ch in text.lower():
    if ch in "aeiou":
        count += 1

print("Vowels =", count)

#Duplicate from the list
numbers = [1, 2, 2, 3, 4, 4, 5]

unique = []

for num in numbers:
    if num not in unique:
        unique.append(num)

print(unique)

#frequency of the string 
text = "banana"

frequency = {}

for ch in text:
    if ch in frequency:
        frequency[ch] += 1
    else:
        frequency[ch] = 1

print(frequency)

#membership operator
numbers = [10, 20, 30, 40, 50]
print(30 in numbers)      
print(60 in numbers)
print(60 not in numbers)

#Arthmetice oprator
a = 10
b = 5
print("Addition =", a + b)
print("Subtraction =", a - b)
print("Multiplication =", a * b)
print("Division =", a / b)
print("Modulus =", a % b
print("Floor Division =", a // b)

