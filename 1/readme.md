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

## Declaring Variables
Python is an "untyped" language, meaning you do not need to declare types of variables. 
```
x = "hello"          # declare a string
y = 1                # declare an int
z = ["50", y, 7.6]   # declare a list containing [string, variable, float] types
```

## Operations on Variables
Operations on variables are done two different ways. One method uses operators such as `+`, or `-`. The other method uses dot-notation to access attributes and methods of an object. Each different variable type has a different set of supported operations. Here are some examples...
- Math on numbers: 
```
x = 1
y = 2
z = 5
n = (x + y) * z  # -> 15
```
- Removing a character from the end of a string:
```
foo = "abc."
foo = foo.strip(".")  # -> "abc"
```
- Adding characters to a string
```
name = "first"
name = name + "last"  # -> "firstlast"
```
We'll see more as we go!

# Lists
Python has a powerful builtin type, `list` which allows you to store multiple items in a single variable, and access individual items or selections of multiple items easily

## Creating a list
Lists are created using square brackets to surround the entries.
```
mylist = ["dog", "cat", "frog"]
```

## Accessing list items
Python `list`s are ordered. The first item lives at index `0`, the next at index `1`, and so on. Trying to access an item which does not exist will result in an error.
```
mylist[0]  # -> "dog"
mylist[2]  # -> "frog"
mylist[5]  # -> ERROR!
```
