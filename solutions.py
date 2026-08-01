#Question 1: Invert a Dictionary
def invert(dict1):
    d = {}
    for key, val in dict1.items():
        d[val] = key

    print(d)

w = {"a": 1, "b": 2, "c": 3}
invert(w)

#Question 2: Filter Dictionary by Value
def filter(dict1, threshold):
    result = {}
    for key, val in dict1.items():
        if val > threshold:
            result[key] = val

    print(result)

products = {"pen": 8, "cup": 35, "bag": 2, "box": 70}
threshold = 15
filter(products, threshold)

#Question 3: Count Vowels and Consonants
def count_v_w(s):
    vowel = 'aeiou'
    d = {'consonants': 0, 'vowels': 0}
    s = s.lower()

    for elt in s:
        if elt.isalpha():
            if elt in vowel:
                d['vowels'] += 1
            else:
                d['consonants'] += 1

    print(d)

t = "hello world"
count_v_w(t)

# Question 4: Find All Keys with Maximum Value
def max_keys(dict1):
    mx_val = float('-inf')

    for val in dict1.values():
        if val > mx_val:
            mx_val = val

    ans = []
    for key, val in dict1.items():
        if val == mx_val:
            ans.append(key)
    ans.sort()

    print(ans)

Input = {"marker": 90, "pen": 10, "box": 90,  "sharpener": 5}
max_keys(Input)

#Question 5: Sum of Values in a Dictionary
def summmm(dict1):
    result = 0
    for val in dict1.values():
        result += val

    print(result)

Input = {"food": 200, "rent": 1000, "household": 150, "others": 300}
summmm(Input)

#Question 6 : Common Keys Between Two Dictionaries
def common_keys(dict1, dict2):
    result = []
    for key in dict1.keys():
        if key in dict2.keys():
            result.append(key)

    result.sort()
    print(result)

d = {"a": 1, "b": 2, "c": 3}
b = {"b": 5, "c": 6, "d": 7}
common_keys(d, b)