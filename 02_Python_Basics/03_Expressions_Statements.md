# Expressions and Statements in Python

---

## 1. Introduction

In Python, a program is made up of **expressions** and **statements**.
Understanding the difference between them is very important for writing correct programs.

---

## 2. Expressions

### 2.1 What is an Expression?

An **expression** is a combination of **values, variables, and operators** that is **evaluated to produce a result**.

➡ Expressions always return a value.

---

### 2.2 Types of Expressions

---

## a) Arithmetic Expressions

Arithmetic expressions perform mathematical calculations.

#### Operators Used
`+  -  *  /  %  //  **`

#### Example:
```python
x = 10 + 5
y = 20 * 2
z = (10 + 5) * 2
```
Output:
```python
x = 15
y = 40
z = 30
```

## b) Relational (Comparison) Expressions

Used to compare two values.
They return True or False.

Operators Used

> < >= <= == !=

Example:
```python
a = 10
b = 5
result = a > b
```
```python
Output:

True
```

## c) Logical Expressions

Logical expressions combine conditions.

Operators Used

> and or not

Example:
```python
x = 10
y = 5
result = (x > y) and (y > 2)
```
```python
Output:

True
```

## d) Assignment Expressions

Assignment expressions assign values to variables.

Operators Used

> = += -= *= /= %=

Example:
```python
x = 10
x += 5
```
```python
Output:

x = 15
```

## e) Bitwise Expressions

Used to perform operations at the binary level.

Operators Used

> & | ^ ~ << >>

Example:
```python
a = 5
b = 3
result = a & b
```
```python
Output:

1
```

## f) Conditional (Ternary) Expressions

Used to make decisions in a single line.

Syntax:

> value_if_true if condition else value_if_false

Example:
```python
x = 10
result = "Even" if x % 2 == 0 else "Odd"
```
```python
Output:

Even
```

## g) Membership Expressions

Used to check membership in sequences.

Operators Used

> in, not in

Example:
```python
list1 = [1, 2, 3]
result = 2 in list1
```
```python
Output:

True
```

## h) Identity Expressions

Used to compare memory locations..

Operators Used

> is, is not

Example:
```python
a = 10
b = 10
result = a is b
```
```python
Output:

True
```

## 3. Statements

### 3.1 What is a Statement?

A statement is an instruction that performs an action.
Statements do not return a value directly.

### 3.2 Types of Statements

## a) Assignment Statement

Used to assign values to variables.

Example:

    x = 10

## b) Conditional Statements

Used to make decisions.

Types:

    if

    if-else

    if-elif-else

Example:
```python
x = 10

if x > 5:
    print("x is greater than 5")
else:
    print("x is less than or equal to 5")
```
```python
Output:

x is greater than 5
```

## c) Looping Statements

Used to repeat a block of code.

Types:

    for loop

    while loop

Example (for loop):
```python
for i in range(3):
    print(i)
```
```python
Output:

0
1
2
```
## d) Control Flow Statements

Used to control loop execution.

Types:

    break

    continue

    pass

Example:
```py
for i in range(5):
    if i == 3:
        break
    print(i)
```
```py
Output:

0
1
2
```

## e) Function Definition Statement

Used to define a function.

Example:
```py
def add(a, b):
    return a + b

print(add(2, 3))
```
```py
Output:

5
```

## f) Import Statement

Used to import modules.

Example:
```py
import math
print(math.sqrt(16))
```
```py
Output:

4.0
```

## 4. Difference Between Expression and Statement

### Expression	Statement

Produces a value	Performs an action

Can be part of a statement	Cannot be part of an expression

    Example: 10 + 5	Example: x = 10

## 5. Uses of Expressions and Statements

Expressions are used for:

    Calculations

    Conditions

    Assigning values

    Decision making

Statements are used for:

    Program control

    Repetition

    Decision making

    Defining functions and classes

## 6. Summary

    Expressions evaluate to values

    Statements perform actions

    Python programs are a combination of both

    Understanding them helps write efficient code

