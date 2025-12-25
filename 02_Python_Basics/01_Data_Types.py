print("========== PYTHON DATA TYPES ==========\n")

# --------------------------------------------------
# 1. INTRODUCTION TO DATA TYPES
# --------------------------------------------------

print("1. What are Data Types?")
print("Data types define the type of data a variable can store.\n")

# --------------------------------------------------
# 2. NUMERIC DATA TYPES
# --------------------------------------------------

print("2. Numeric Data Types\n")

# a) int
a = 10
print("int example:")
print("a =", a)
print("Type of a:", type(a), "\n")

# b) float
b = 3.14
print("float example:")
print("b =", b)
print("Type of b:", type(b), "\n")

# c) complex
c = 2 + 3j
print("complex example:")
print("c =", c)
print("Type of c:", type(c))
print("Real part:", c.real)
print("Imaginary part:", c.imag, "\n")

# --------------------------------------------------
# 3. BOOLEAN DATA TYPE
# --------------------------------------------------

print("3. Boolean Data Type\n")

x = True
y = False

print("x =", x, "Type:", type(x))
print("y =", y, "Type:", type(y))
print("x > y:", x > y, "\n")

# --------------------------------------------------
# 4. NONE DATA TYPE
# --------------------------------------------------

print("4. None Data Type\n")

n = None
print("n =", n)
print("Type of n:", type(n), "\n")

# --------------------------------------------------
# 5. STRING DATA TYPE
# --------------------------------------------------

print("5. String Data Type\n")

s = "Python Programming"

print("String:", s)
print("Type:", type(s))
print("Length:", len(s))
print("Uppercase:", s.upper())
print("Lowercase:", s.lower())
print("First character:", s[0])
print("Last character:", s[-1])
print("Slicing [0:6]:", s[0:6], "\n")

# --------------------------------------------------
# 6. LIST DATA TYPE
# --------------------------------------------------

print("6. List Data Type\n")

lst = [10, 20, 30, "Python", True]

print("List:", lst)
print("Type:", type(lst))
print("Access element at index 1:", lst[1])

lst.append(40)
print("After append:", lst)

lst.remove(20)
print("After remove 20:", lst, "\n")

# --------------------------------------------------
# 7. TUPLE DATA TYPE
# --------------------------------------------------

print("7. Tuple Data Type\n")

tpl = (10, 20, 30, "Python")

print("Tuple:", tpl)
print("Type:", type(tpl))
print("Access element:", tpl[2])
print("Tuples are immutable (cannot be changed)\n")

# --------------------------------------------------
# 8. SET DATA TYPE
# --------------------------------------------------

print("8. Set Data Type\n")

st = {10, 20, 30, 30, 40}

print("Set:", st)
print("Type:", type(st))
print("Sets remove duplicate values")

st.add(50)
print("After add 50:", st, "\n")

# --------------------------------------------------
# 9. FROZENSET DATA TYPE
# --------------------------------------------------

print("9. Frozenset Data Type\n")

fs = frozenset([1, 2, 3, 3, 4])
print("Frozenset:", fs)
print("Type:", type(fs))
print("Frozenset is immutable\n")

# --------------------------------------------------
# 10. DICTIONARY DATA TYPE
# --------------------------------------------------

print("10. Dictionary Data Type\n")

student = {
    "name": "Amit",
    "age": 21,
    "branch": "CSE"
}

print("Dictionary:", student)
print("Type:", type(student))
print("Access value using key:", student["name"])

student["age"] = 22
print("After updating age:", student)

student["college"] = "ABC University"
print("After adding new key:", student, "\n")

# --------------------------------------------------
# 11. TYPE CONVERSION (TYPE CASTING)
# --------------------------------------------------

print("11. Type Casting\n")

a = "100"
b = int(a)
c = float(b)

print("String to int:", b, "Type:", type(b))
print("Int to float:", c, "Type:", type(c))

x = 10
y = str(x)
print("Int to string:", y, "Type:", type(y), "\n")

# --------------------------------------------------
# 12. MUTABLE vs IMMUTABLE DATA TYPES
# --------------------------------------------------

print("12. Mutable vs Immutable\n")

print("Mutable Data Types:")
print("List, Set, Dictionary\n")

print("Immutable Data Types:")
print("int, float, string, tuple, frozenset\n")

# --------------------------------------------------
# 13. CHECKING DATA TYPE
# --------------------------------------------------

print("13. Checking Data Type using type()\n")

value = 123
print("value =", value)
print("Type:", type(value), "\n")

# --------------------------------------------------
# 14. SUMMARY
# --------------------------------------------------

print("14. Summary")
print("""
Numeric      -> int, float, complex
Boolean      -> bool
Text         -> str
Sequence     -> list, tuple
Set          -> set, frozenset
Mapping      -> dict
Special      -> NoneType
""")

print("========== END OF DATA TYPES ==========")
