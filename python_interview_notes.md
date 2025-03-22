# Python 3 Interview Notes
https://chatgpt.com/share/67d04418-29c8-800d-b80b-5c5637e417a5

## 1. Python Basics

### What is Python?
- Python is a high-level, interpreted, dynamically typed programming language.
- It supports object-oriented, imperative, functional, and procedural programming paradigms.
- Python is widely used in web development, data science, automation, scripting, and artificial intelligence.

### Python Features
- **Easy to Learn & Readable** – Uses English-like syntax.
- **Dynamically Typed** – No need to define variable types.
- **Interpreted Language** – Executes code line by line.
- **Cross-Platform** – Runs on Windows, macOS, and Linux.
- **Large Standard Library** – Includes modules for OS, networking, databases, etc.
- **Open Source & Community Support** – Actively maintained by developers worldwide.

### Python Syntax Basics

#### Variables & Assignment
```python
x = 10        # Integer
y = 3.14      # Float
name = "John" # String
is_active = True # Boolean

# Printing & Input
print("Hello, Python!")  # Output text
age = input("Enter your age: ")  # Get user input

# Data Structures
Lists (Dynamic Arrays)
Ordered, mutable (modifiable).
Can store elements of different types.
Methods: append(), pop(), remove(), sort(), reverse().

my_list = [1, 2, 3, "Python"]
my_list.append(4)  # Adds 4 to the end
my_list.pop(2)     # Removes the element at index 2

# Tuples (Immutable Lists)
Ordered but immutable (cannot be modified).
Faster than lists.
Used for read-only collections.

my_tuple = (10, 20, "hello")
print(my_tuple[1])  # Output: 20

# Sets (Unordered Unique Elements)
Stores only unique values.
Unordered and does not allow duplicates.
Methods: add(), remove(), union(), intersection(), difference().

my_set = {1, 2, 3, 4}
my_set.add(5)  # Adds 5 to the set
print(my_set)

# Dictionaries (Key-Value Pairs)
Stores key-value pairs.
Methods: get(), keys(), values(), items(), pop().

student = {"name": "Alice", "age": 22, "grade": "A"}
print(student["name"])  # Output: Alice

## Control Flow (If-Else, Loops)
Conditional Statements
age = 18
if age >= 18:
    print("You can vote.")
elif age > 16:
    print("You can drive.")
else:
    print("Too young!")
Loops
# For Loop
for i in range(5):
    print(i)  # Prints 0 to 4
# While Loop
x = 5
while x > 0:
    print(x)
    x -= 1

# List Comprehension
A shorter way to create lists.

squares = [x**2 for x in range(5)]
print(squares)  # [0, 1, 4, 9, 16]

## Functions
Code Reuse with Functions
Can return values.
Supports default arguments.

def greet(name="Guest"):
    return "Hello " + name
print(greet("Alice"))  # Output: Hello Alice

## Lambda Functions
Anonymous one-liner functions.

square = lambda x: x**2
print(square(4))  # Output: 16

## Args & Kwargs
Flexible argument passing.

def sum_numbers(*args):
    return sum(args)

print(sum_numbers(1, 2, 3))  # Output: 6

## Object-Oriented Programming (OOP)
Class & Object

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def show(self):
        return f"{self.brand} {self.model}"

my_car = Car("Toyota", "Camry")
print(my_car.show())  # Output: Toyota Camry

# Inheritance
python
Copy
class ElectricCar(Car):
    def __init__(self, brand, model, battery):
        super().__init__(brand, model)
        self.battery = battery

## Exception Handling
Handling Runtime Errors

try:
    num = int(input("Enter a number: "))
    print(10 / num)
except ZeroDivisionError:
    print("Cannot divide by zero.")
except ValueError:
    print("Invalid input.")
finally:
    print("Execution complete.")

## File Handling
Reading a File

with open("data.txt", "r") as file:
    content = file.read()
    print(content)

Writing to a File

with open("data.txt", "w") as file:
    file.write("Hello, World!")

## Modules & Packages
Importing Modules

import math
print(math.sqrt(25))  # Output: 5.0

Creating a Custom Module
mymodule.py

def add(x, y):
    return x + y

Using the Module

from mymodule import add
print(add(3, 4))  # Output: 7

