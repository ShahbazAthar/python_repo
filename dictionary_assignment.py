# # Q1: Enter Name and Percentage Marks in a dictionary and display it
# def func1():
#     student = {}
#     while True:
        
#         name = input("enter name: ")

#         if not name:
#             break

#         while True:
#             try:
#                 percentage = float(input("enter percentage: "))
#                 if not (0 <= percentage <= 100):
#                     print("percentage out of range")
#                 else:
#                     break
                    
#             except ValueError:
#                 print('enter valid percentage')


#         student[name] = percentage

#     print(student)

# func1()

# # Q2: Number of occurrences of each letter in a given string
# def func2():
#     text = input("enter a string: ")

#     letter_count = {}
#     for ch in text:
#         if ch.isalpha():
#             letter_count[ch] = letter_count.get(ch, 0) + 1

#     for letter, count in letter_count.items():
#         print(letter, ":", count)

# func2()

# # Q3: Number of occurrences of each vowel in a given string
# def func3():
#     text = input("enter a string: ")

#     vowels = "aeiou"
#     vowel_count = {}
#     for v in vowels:
#         vowel_count[v] = 0

#     for ch in text.lower():
#         if ch in vowels:
#             vowel_count[ch] += 1

#     for vowel, count in vowel_count.items():
#         print(vowel, ":", count)

# func3()

# # Q4: Accept student names & marks, store in dictionary,
# #    then look up marks by entering a student name

# def func4():
#     student = {}
#     while True:

#         name = input("enter name: ")

#         if not name:
#             break

#         while True:
#             try:
#                 marks = float(input("enter marks: "))
#                 if not (0 <= marks <= 100):
#                     print("marks out of range")
#                 else:
#                     break

#             except ValueError:
#                 print('enter valid marks')

#         student[name] = marks

#     search_name = input("enter student name: ")
#     if search_name in student:
#         print("marks of", search_name, ":", student[search_name])
#     else:
#         print("no record found for", search_name)

# func4()

# Q5: Tabular comparison of List, Tuple, Set, Frozenset, Dictionary

data = {
    "Syntax": ["[ ]", "( )", "{ }", "frozenset()", "{key:value}"],
    "Ordered": ["Yes", "Yes", "No", "No", "Yes"],
    "Mutable": ["Yes", "No", "Yes", "No", "Yes"],
    "Allow Duplicates": ["Yes", "Yes", "No", "No", "No"],
    "Indexed": ["Yes", "Yes", "No", "No", "By key"],
    "Heterogeneous": ["Yes", "Yes", "Yes", "Yes", "Yes"],
    "Hashable": ["No", "Yes", "No", "Yes", "No"],
    "Can be dict key": ["No", "Yes", "No", "Yes", "No"],
    "Can be nested": ["Yes", "Yes", "No", "Yes", "Yes"],
    "Supports slicing": ["Yes", "Yes", "No", "No", "No"],
    "Lookup Speed": ["O(n)", "O(n)", "O(1)", "O(1)", "O(1)"],
    "Stores": ["Items", "Items", "Unique", "Unique", "Key-Value"],
    "Typical Use": ["Sequence", "Fixed", "Unique", "Const", "Mapping"],
}

print("Property", "\t", "List", "\t", "Tuple", "\t", "Set", "\t", "Frozenset", "\t", "Dictionary")

for key, value in data.items():
    print(key, end="\t")
    for item in value:
        print(item, end="\t")
    print()