# Introduction to Python!

## Why use Python?
- It is a simple language - you can do more with less
- Wide selection of libraries and frameworks 
- Very popular in academia and industry

## What do people use Python for?
- Web development: building apps, APIs, and websites
- Data science: machine learning, artificial intelligence
- System Management/Automation: writing custom scripts to manage computers
- Computer Graphics: creating graphs and visuals
- **Internet of Things**: Python is supported on many devices and sensors

# Writing Python Code
Python is an "interpreted" language. The Python interpreter reads and executes your code line-by-line. The easiest way to run Python code is by writing it in a `.py` file, such as `program.py`, and running it with the shell command `python program.py`
### Declaring Variables
Python is an "untyped" language, meaning you do not need to declare types of variables. 
```python
x = "hello"          # declare a string
y = 1                # declare an int
z = ["50", y, 7.6]   # declare a list containing [string, variable, float] types
```
### Operations on Variables
Operations on variables are done two different ways. One method uses operators such as `+`, or `-`. The other method uses dot-notation to access attributes and methods of an object. Each different variable type has a different set of supported operations. Here are some examples...
- Math on numbers: 
```python
x = 1
y = 2
z = 5
n = (x + y) * z 
print(n)  # -> 15
```
- Removing a character from the end of a string:
```python
foo = "abc."
foo = foo.strip(".")  
print(foo)  # -> "abc"
```
- Adding characters to a string
```python
name = "first"
name = name + "last"  
print(name)  # -> "firstlast"
```
We'll see more as we go!

# modules and imports
One of the strengths of Python is the amount of libraries it supports. This allows you to use code from another module in your program. You import modules using the `import` keyword, typically at the beginning of the file.
- importing `math` and using the `pow` function
```python
import math
x = math.pow(2,3)  # 2*2*2
print(x)           # -> 8.0
```
- importing the `date` submodule from `datetime` to determine today's date
```python
from datetime import date
today = date.today()
print(today)  # -> "2022-11-16"
```

# Lists
Python has a powerful builtin type, `list` which allows you to store multiple items in a single variable, and access individual items or selections of multiple items easily
### Creating a list
Lists are created using square brackets to surround the entries.
```python
mylist = ["dog", "cat", "frog", "log"]
mylist.append("bog")
print(mylist)  # -> ["dog", "cat", "frog", "log", "bog"]
```
### Accessing list items
Python `list`s are ordered. The first item is positioned at index `0`, the next at index `1`, and so on. You can access a "slice" of multiple elements with the syntax `[start:stop]`. Trying to access an item which does not exist will result in an error.
```python
print(mylist[0])    # -> "dog"
print(mylist[2])    # -> "frog"
print(mylist[1:3])  # -> ["cat", "frog"]
print(mylist[5])    # -> ERROR!
```
### Deleting list items
You can delete an item by using the `del` keyword
```python
del mylist[0]     # -> mylist = ["cat", "frog", "log", "bog"]
print(mylist[0])  # -> "cat"
```

# Dictionaries
Another powerful builtin of Python, the `dict`. Dictionaries are "key:value" pairs, with the "value" being hash mapped to the "key". 
### Creating a `dict`
Write the initial pairs inside of curly braces
```python
data = {"dog": "woof", "cat": "meow"}
data["cow"] = "moo"
print(data)  # -> {"dog": "woof", "cat": "meow", "cow": "moo"}
```
### Get a list of the keys and values
```python
keys = dict.keys()
print(list(keys))  # -> ["dog", "cat", "cow"]
vals = dict.vals()
print(list(vals))  # -> ["woof", "meow", "moo"]
```

# Determining the length of `string`s, `list`s, `dict`s: `len()`
The `len()` builtin function is very handy. Allows you to check the length of a `str`, or the number of elements in a `list` or `dict`. Useful for conditionals and loops. 
```python
a = "hello"
b = [1, "xyz", 5.0]
c = {"dog": "woof"}
print(len(a))  # -> 5
print(len(b))  # -> 3
print(len(c))  # -> 1
```

# Logic and Equality in Python
One of the most common things you'll do as a programmer is check if objects or values are equal.
```python
password = "badpassword"
print(password == "goodpassword")  # -> False
```
You can incorporate the `and`, `or`, and `not` keywords to check multiple conditions.
```python
price = 10
print(price > 1 and price < 100)  # -> True
```

# `if`, `elif`, and `else` statements
You'll often want your program to do different things depending on some variable or input. You can control the flow of your program using `if` statements, which execute code only *if* their condition is `True`. An `if` statement can be on its own, or followed by an `elif` ("else if"), or `else` statement.
```python
price = 16
if price <= 3:
	print("That's pretty cheap!")
elif price > 3 and price <= 15:
	print("Ok, that's a fair price")
elif price > 15 and price <= 20:
	print("You're asking a little much...")
else:
	print("You're out of your mind!") 
# - > "You're asking a little much..."
```

# 
