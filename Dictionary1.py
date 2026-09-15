dict = {'a': 1, 'b': 2, 'c': 3}
print(dict.values())  # Output: dict_values([1, 2, 3])
print(*dict.values())  # Output: 1 2 3
print(dict.items())  # Output: dict_items([('a', 1), ('b', 2), ('c', 3)])

data1 = {'id': [1, 2, 3], 'Name': ['Alice', 'Bob', 'Charlie']} 
print(*data1.values())  # Output: [1, 2, 3] ['Alice', 'Bob', 'Charlie']
print(data1.values())  # Output: [[1, 2, 3], ['Alice', 'Bob', 'Charlie']]
# ** unpacks dicts into keyword arguments (e.g., func(**my_dict))
"""
In function definitions, **kwargs captures any number of keyword arguments (like name="Alice")
passed to the function, storing them as a dictionary where keys are argument names and values are the provided values.
"""
def greet(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

greet(name="Alice", age=25, city="Delhi", id = 101)
# Output:
# name: Alice
# age: 25
# city: Delhi

