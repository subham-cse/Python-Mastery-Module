# Python Variables and Naming Rules

---

## 1. What is a Variable?

A **variable** in Python is a name given to a memory location that stores data.
It is used to hold values so that they can be reused and manipulated in a program.

### Example:

```python
x = 10
name = "Python"
```

Here:

    x stores the value 10

    name stores the string "Python"


## 2. Creating Variables in Python

Python does not require explicit declaration of variables.
A variable is created when a value is assigned to it.
Syntax:
```
variable_name = value
```
Example:
```python
age = 20
pi = 3.14
is_valid = True
```

## 3. Multiple Variable Assignment

### a) Assigning same value to multiple variables

```
a = b = c = 10
```

b) Assigning different values at once

```
x, y, z = 1, 2, 3
```

## 4. Dynamic Typing in Python

Python is dynamically typed, meaning the data type of a variable can change.
Example:

```python
x = 10
x = "Python"
```

Here, x first stores an integer, then a string.

## 5. Rules for Naming Variables in Python

Python has strict rules for naming variables.

### ✅ Valid Rules

Variable names must start with:
```
a letter (a–z or A–Z)
or an underscore _
```

Variable names can contain: letters, numbers, underscores

Variable names are case-sensitive

```age and Age are different```


Variable names can be of any length

### ❌ Invalid Rules

Variable names cannot start with a number

    value = 10   ❌

Variable names cannot contain special characters

    total$ = 100   ❌
    my-name = "A"  ❌

Variable names cannot be Python keywords

    if = 10        ❌
    class = "CS"   ❌

## 6. Valid and Invalid Variable Name Examples

### ✅ Valid Variable Names

    age
    student_name
    _total
    marks123
    PI_VALUE

### ❌ Invalid Variable Names

    2marks
    student-name
    total@
    for

## 7. Naming Conventions (Best Practices)

Although Python allows many names, follow best practices:

✔ Use meaningful names

    marks = 90
    total_students = 60

### ❌ Avoid meaningless names

    x = 90
    y = 60

✔ Use lowercase with underscores (snake_case)

    student_marks
    total_price

✔ Use uppercase for constants

    PI = 3.14
    GRAVITY = 9.8

## 8. Keywords in Python (Cannot be Used as Variable Names)

Some Python keywords include:

    if, else, while, for, break, continue,
    class, def, return, import, True, False, None

These words have predefined meanings in Python.

## 9. Checking Variable Type

You can check the type of a variable using type().

Example:
```python
x = 10
print(type(x))
```
```python
Output:

<class 'int'>
```

## 10. Summary

Variables store data values

Python variables are dynamically typed

Naming rules must be followed strictly

Meaningful variable names improve readability

Keywords cannot be used as variable names