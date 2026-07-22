'''    
- *args allows a function to accept any number of 
positional arguments, which are stored as a tuple.

- **kwargs allows a function to accept any number
    of keyword arguments, which are stored as a dictionary.
'''

def students(**kwargs):
    print(kwargs)

students(name = "Anil", age =  66)

def add(*args):
    total = 0

    for num in args:
        total += num

    return total

print(add(3 + 7 + 6))

def display(name, *marks, **details):
    print(name)
    print(marks)
    print(details)

display("Shahbaz", 12, 79, 9, 77, hometown = "gorakhpur", hobby = 'cricket')

''' Order of parameters
The order should be:

def function(normal_args, *args, **kwargs):
    pass

Example:
def demo(a, b, *args, **kwargs):
    pass
'''