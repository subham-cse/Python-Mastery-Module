print("========== EXPRESSIONS AND STATEMENTS IN PYTHON ==========\n")

# --------------------------------------------------
# 1. EXPRESSIONS
# --------------------------------------------------

print("1. EXPRESSIONS\n")
print("An expression is a combination of values, variables, and operators")
print("that is evaluated to produce a result.\n")

# --------------------------------------------------
# 1.1 Arithmetic Expressions
# --------------------------------------------------

print("1.1 Arithmetic Expressions")

a = 10
b = 3

print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)
print("a // b =", a // b)
print("a % b =", a % b)
print("a ** b =", a ** b, "\n")

# --------------------------------------------------
# 1.2 Relational (Comparison) Expressions
# --------------------------------------------------

print("1.2 Relational Expressions")

x = 10
y = 5

print("x > y :", x > y)
print("x < y :", x < y)
print("x == y:", x == y)
print("x != y:", x != y)
print("x >= y:", x >= y)
print("x <= y:", x <= y, "\n")

# --------------------------------------------------
# 1.3 Logical Expressions
# --------------------------------------------------

print("1.3 Logical Expressions")

p = True
q = False

print("p and q:", p and q)
print("p or q :", p or q)
print("not p  :", not p, "\n")

# --------------------------------------------------
# 1.4 Assignment Expressions
# --------------------------------------------------

print("1.4 Assignment Expressions")

n = 10
print("Initial n =", n)

n += 5
print("After n += 5 ->", n)

n -= 3
print("After n -= 3 ->", n, "\n")

# --------------------------------------------------
# 1.5 Bitwise Expressions
# --------------------------------------------------

print("1.5 Bitwise Expressions")

a = 5   # 0101
b = 3   # 0011

print("a & b =", a & b)
print("a | b =", a | b)
print("a ^ b =", a ^ b)
print("~a    =", ~a)
print("a << 1 =", a << 1)
print("a >> 1 =", a >> 1, "\n")

# --------------------------------------------------
# 1.6 Conditional (Ternary) Expression
# --------------------------------------------------

print("1.6 Conditional (Ternary) Expression")

num = 10
result = "Even" if num % 2 == 0 else "Odd"
print("Number:", num)
print("Result:", result, "\n")

# --------------------------------------------------
# 1.7 Membership Expressions
# --------------------------------------------------

print("1.7 Membership Expressions")

data = [1, 2, 3, 4]

print("2 in data    :", 2 in data)
print("5 not in data:", 5 not in data, "\n")

# --------------------------------------------------
# 1.8 Identity Expressions
# --------------------------------------------------

print("1.8 Identity Expressions")

a = 100
b = 100
c = 200

print("a is b     :", a is b)
print("a is not c :", a is not c, "\n")

# --------------------------------------------------
# 2. STATEMENTS
# --------------------------------------------------

print("2. STATEMENTS\n")
print("A statement is an instruction that performs an action.")
print("Statements do not directly return values.\n")

# --------------------------------------------------
# 2.1 Assignment Statement
# --------------------------------------------------

print("2.1 Assignment Statement")

x = 50
print("x =", x, "\n")

# --------------------------------------------------
# 2.2 Conditional Statements
# --------------------------------------------------

print("2.2 Conditional Statements")

marks = 75

if marks >= 40:
    print("Pass")
else:
    print("Fail")

print()

# --------------------------------------------------
# 2.3 if-elif-else Statement
# --------------------------------------------------

print("2.3 if-elif-else Statement")

score = 85

if score >= 90:
    print("Grade: A")
elif score >= 75:
    print("Grade: B")
else:
    print("Grade: C")

print()

# --------------------------------------------------
# 2.4 Looping Statements
# --------------------------------------------------

print("2.4 Looping Statements")

print("for loop example:")
for i in range(3):
    print(i)

print()

print("while loop example:")
i = 0
while i < 3:
    print(i)
    i += 1

print()

# --------------------------------------------------
# 2.5 Control Flow Statements
# --------------------------------------------------

print("2.5 Control Flow Statements")

print("break example:")
for i in range(5):
    if i == 3:
        break
    print(i)

print()

print("continue example:")
for i in range(5):
    if i == 2:
        continue
    print(i)

print()

print("pass example:")
for i in range(3):
    pass
print("pass does nothing but avoids errors\n")

# --------------------------------------------------
# 2.6 Function Definition Statement
# --------------------------------------------------

print("2.6 Function Definition Statement")

def add(a, b):
    return a + b

print("add(5, 3) =", add(5, 3), "\n")

# --------------------------------------------------
# 2.7 Import Statement
# --------------------------------------------------

print("2.7 Import Statement")

import math
print("Square root of 16 =", math.sqrt(16), "\n")

# --------------------------------------------------
# 3. DIFFERENCE BETWEEN EXPRESSIONS AND STATEMENTS
# --------------------------------------------------

print("3. Difference Between Expression and Statement\n")

print("Expression Example: 10 + 5 =", 10 + 5)
x = 10
print("Statement Example : x = 10 (assignment)\n")

# --------------------------------------------------
# 4. SUMMARY
# --------------------------------------------------

print("4. Summary\n")

print("""
✔ Expressions produce values
✔ Statements perform actions
✔ Expressions are part of statements
✔ Python programs use both together
""")

print("========== END OF EXPRESSIONS AND STATEMENTS ==========")
