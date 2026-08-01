nums = [8, 3, 1, 7, 5]
nums.sort()
print(nums)

nums = [8, 3, 1, 7, 5]
nums.sort(reverse = True)
print(nums)

nums = [8, 3, 1, 7, 5]
nums.sort(key = lambda x: -x)
print(nums)

words = ["cat", "elephant", "dog", "apple", "hi"]
words.sort(key = lambda x : (len(x), x))
print(words)

words = ["cat", "elephant", "dog", "apple", "hi"]
words.sort(key = lambda x : (len(x), -ord(x[0])))
print(words)

words = ["bat", "apple", "cat", "dog", "ant", "hi"]
words.sort(key = lambda x : (len(x), x))
print(words)

data = [(1, 9), (3, 2), (2, 5), (8, 1)]
data.sort(key = lambda x : x[1] )
print(data)

data = [(1, 9), (3, 2), (2, 5), (8, 1)]
data.sort(key = lambda x : -x[1] )
print(data)

students = [
    ("Alice", 75),
    ("Bob", 91),
    ("Charlie", 82),
    ("David", 91)
]
students.sort(key = lambda x : (-x[1], x[0]))
print(students)

words = ["apple", "cat", "dog", "banana"]
words.sort(key = lambda x : ord(x[-1]))
print(words)

nums = [-8, 3, -2, 7, -5]
nums.sort(key = lambda x: abs(x))
print(nums)

d = {
    "pen":20,
    "book":5,
    "box":40,
    "pencil":20
}

keys = sorted(d, key = lambda x : (-d[x], x))
print(keys)

d = {
    "pen":20,
    "book":5,
    "box":40,
    "pencil":20
}
result = sorted(d.items(), key = lambda x: (-x[1], x[0]))
print(result)

d = {
    "pen":20,
    "book":5,
    "box":40,
    "pencil":20
}
result = sorted(d.items(), key = lambda x: (x[1], x[0]), reverse = True)
print(result)

d = {
    "pen":20,
    "book":5,
    "box":40,
    "pencil":20
}
result = sorted(d.items(), key = lambda x: (x[1], x[0]))
print(result)

d = {
    "pen":20,
    "book":5,
    "box":40,
    "pencil":20
}
result = sorted(d.items(), key = lambda x: (-x[1], x[0]), reverse = True)
print(result)

people = [
    {"name":"Alice","age":25},
    {"name":"Bob","age":20},
    {"name":"Charlie","age":22}
]
result = sorted(people, key = lambda x : x['age'])
print(result)

people = [
    {"name":"Alice","age":25},
    {"name":"Bob","age":20},
    {"name":"Charlie","age":22}
]
people.sort(key = lambda x : x['age'])
print(people)

people = [
    {"name":"Bob","age":25},
    {"name":"Alice","age":20},
    {"name":"David","age":25},
    {"name":"Charlie","age":20}
]
people.sort(key = lambda x : (x['age'], x['name']))
print(people)

nums = [8, 4, 6, 9, 2, 7]
nums.sort(key = lambda x: x%3)
print(nums)

words = ["Apple", "banana", "Cat", "dog", "ant"]
words.sort(key = lambda x: x.lower())
print(words)

words = ["Apple", "banana", "Cat", "dog", "ant"]
words.sort(key = str.lower)
print(words)

words = [
    "banana",
    "cat",
    "apple",
    "kiwi",
    "orange",
    "bat"
]
words.sort(key = lambda x: (-len(x), sum(1 for elt in x.lower() if elt in 'aeiou'), x.lower()))
print(words)