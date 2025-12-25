# 📊 Data Types in Python

## 📌 Introduction
In Python, **data types** define the kind of value a variable can store.
Python is a **dynamically typed language**, which means the programmer does not need to explicitly declare the data type of a variable. The interpreter automatically determines the data type during program execution.

Understanding data types is essential for:
- Writing correct and error-free programs
- Performing valid operations on data
- Managing memory efficiently
- Building a strong programming foundation

---

## 🔍 What is a Data Type?
A **data type** specifies:
- The type of data stored in a variable
- The operations that can be performed on that data
- How Python interprets the value internally

### Example
```python
x = 10
print(x)
print(type(x))
```
```python
Output:

10
<class 'int'>
```

Here, Python automatically assigns the int data type to the variable x.

## 🧠 Classification of Built-in Data Types

Python provides several built-in data types, grouped as follows:
|Category|Data Types|
|:------:|:--------:|
|Numeric| 	int, float, complex|
|Text	|str|
|Sequence	|list, tuple, range|
|Mapping	|dict|
|Set	|set, frozenset|
|Boolean	|bool|
|None	|NoneType|

## 1️⃣ Numeric Data Types

Numeric data types are used to store numbers.

### 🔹 int (Integer)

Stores whole numbers (positive, negative, or zero).

```python
a = 25
b = -10
c = 0
print(a)
print(b)
print(c)
print(type(a))
```
```python
Output:

25
-10
0
<class 'int'>
```

✔ Integers can be of any length

✔ Limited only by system memory

### 🔹 float (Floating-Point)

Stores numbers with decimal points.

```python
x = 3.14
y = -0.75
print(x)
print(y)
print(type(x))
```
```python
Output:

3.14
-0.75
<class 'float'>
```

✔ Used in scientific and mathematical calculations

✔ Less precise than integers due to decimal representation

### 🔹 complex

Stores complex numbers in the form real + imaginary.

```python
z = 4 + 5j
print(z)
print(type(z))
```
```python
Output:

(4+5j)
<class 'complex'>
```

✔ j represents the imaginary part

✔ Used in advanced mathematical applications

## 2️⃣ Text Data Type

### 🔹 str (String)

Used to store textual data enclosed in single, double, or triple quotes.

```python
name = "Python"
message = 'Learning Python'
print(name)
print(message)
print(type(name))
```
```python
Output:

Python
Learning Python
<class 'str'>
```

✔ Strings are immutable

✔ Indexing and slicing are supported

## 3️⃣ Sequence Data Types

Sequence data types store collections of values.

### 🔹 list

An ordered and mutable collection of elements.

```python
numbers = [10, 20, 30, 40]
print(numbers)
print(type(numbers))
```
```python
Output:

[10, 20, 30, 40]
<class 'list'>
```

✔ Allows duplicate values

✔ Elements can be modified

### 🔹 tuple

An ordered and immutable collection of elements.

```python
coordinates = (5, 10)
print(coordinates)
print(type(coordinates))
```
```python
Output:

(5, 10)
<class 'tuple'>
```

✔ Faster than lists

❌ Elements cannot be changed

### 🔹 range

Represents a sequence of numbers.

```python
r = range(1, 6)
print(list(r))
print(type(r))
```
```python
Output:

[1, 2, 3, 4, 5]
<class 'range'>
```

✔ Commonly used in loops

## 4️⃣ Mapping Data Type

### 🔹 dict (Dictionary)

Stores data as key–value pairs.

```python
student = {
    "name": "Amit",
    "age": 21,
    "course": "Python"
}
print(student)
print(type(student))
```
```python
Output:

{'name': 'Amit', 'age': 21, 'course': 'Python'}
<class 'dict'>
```

✔ Keys must be unique

✔ Values can be modified

## 5️⃣ Set Data Types

### 🔹 set

An unordered collection of unique elements.

```python
values = {1, 2, 3, 3, 4}
print(values)
print(type(values))
```
```python
Output:

{1, 2, 3, 4}
<class 'set'>
```

✔ Automatically removes duplicates

❌ Does not support indexing

### 🔹 frozenset

An immutable version of a set.

```python
fs = frozenset([1, 2, 3])
print(fs)
print(type(fs))
```
```python
Output:

frozenset({1, 2, 3})
<class 'frozenset'>
```

✔ Cannot be modified after creation

## 6️⃣ Boolean Data Type

### 🔹 bool

Represents logical values: True or False.

```python
is_python_easy = True
print(is_python_easy)
print(type(is_python_easy))
```
```python
Output:

True
<class 'bool'>
```

✔ Used in conditional statements and decision making

## 7️⃣ None Data Type

### 🔹 NoneType

Represents the absence of a value.

```python
result = None
print(result)
print(type(result))
```
```python
Output:

None
<class 'NoneType'>
```

✔ Commonly used as a placeholder or default value

## 🔎 Checking Data Type Using type()

The type() function is used to determine the data type of a variable.

```python
x = 50
print(type(x))
```
```python
Output:

<class 'int'>
```

## 🧠 Summary Table

|Data Type|	Mutable	Example|
|:-------:|:--------------:|
|int	| 10|
|float	|	3.5|
|complex	|	2+3j|
|str	|	"Python"|
|list	|	[1, 2]|
|tuple	|	(1, 2)|
|dict	|	{"a":1}|
|set	|	{1, 2}|
|frozenset	|	frozenset([1,2])|
|bool	|	True|
|NoneType	|	None|
