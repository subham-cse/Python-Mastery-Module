print("========== PYTHON VARIABLES & NAMING RULES ==========\n")

# --------------------------------------------------
# 1. WHAT IS A VARIABLE?
# --------------------------------------------------

print("1. What is a Variable?\n")

x = 10
name = "Python"

print("x =", x)
print("name =", name)
print("Type of x:", type(x))
print("Type of name:", type(name), "\n")

# --------------------------------------------------
# 2. VARIABLE ASSIGNMENT
# --------------------------------------------------

print("2. Variable Assignment\n")

a = 5
b = 3.14
c = True

print("a =", a)
print("b =", b)
print("c =", c, "\n")

# --------------------------------------------------
# 3. MULTIPLE VARIABLE ASSIGNMENT
# --------------------------------------------------

print("3. Multiple Variable Assignment\n")

# Same value to multiple variables
x = y = z = 100
print("x =", x, "y =", y, "z =", z)

# Different values to multiple variables
p, q, r = 1, 2, 3
print("p =", p, "q =", q, "r =", r, "\n")

# --------------------------------------------------
# 4. DYNAMIC TYPING
# --------------------------------------------------

print("4. Dynamic Typing in Python\n")

var = 10
print("var =", var, "Type:", type(var))

var = "Python"
print("var =", var, "Type:", type(var), "\n")

# --------------------------------------------------
# 5. VARIABLE NAMING RULES (VALID)
# --------------------------------------------------

print("5. Valid Variable Names\n")

age = 20
student_name = "Amit"
_total = 500
marks123 = 85
PI_VALUE = 3.14

print("age =", age)
print("student_name =", student_name)
print("_total =", _total)
print("marks123 =", marks123)
print("PI_VALUE =", PI_VALUE, "\n")

# --------------------------------------------------
# 6. VARIABLE NAMING RULES (INVALID - SHOWN AS TEXT)
# --------------------------------------------------

print("6. Invalid Variable Names (Explanation Only)\n")

print("❌ 1value  -> cannot start with a number")
print("❌ total$  -> special characters not allowed")
print("❌ my-name -> hyphen not allowed")
print("❌ for     -> keyword cannot be used\n")

# --------------------------------------------------
# 7. CASE SENSITIVITY
# --------------------------------------------------

print("7. Case Sensitivity in Variables\n")

value = 50
Value = 100

print("value =", value)
print("Value =", Value)
print("Variables are case-sensitive\n")

# --------------------------------------------------
# 8. KEYWORDS CANNOT BE VARIABLE NAMES
# --------------------------------------------------

print("8. Keywords as Variable Names\n")

print("Examples of keywords:")
print("if, else, for, while, class, def, return, True, False, None\n")

# --------------------------------------------------
# 9. GOOD VS BAD VARIABLE NAMES
# --------------------------------------------------

print("9. Good vs Bad Variable Names\n")

# Bad naming
x = 90
y = 5
print("Bad naming example:")
print("x =", x, "y =", y)

# Good naming
total_marks = 90
number_of_subjects = 5
print("Good naming example:")
print("total_marks =", total_marks)
print("number_of_subjects =", number_of_subjects, "\n")

# --------------------------------------------------
# 10. CONSTANTS (BY CONVENTION)
# --------------------------------------------------

print("10. Constants in Python (By Convention)\n")

PI = 3.14159
GRAVITY = 9.8

print("PI =", PI)
print("GRAVITY =", GRAVITY)
print("Constants are written in uppercase by convention\n")

# --------------------------------------------------
# 11. CHECKING VARIABLE TYPE
# --------------------------------------------------

print("11. Checking Variable Type\n")

data = 123
print("data =", data)
print("Type of data:", type(data), "\n")

# --------------------------------------------------
# 12. SUMMARY
# --------------------------------------------------

print("12. Summary\n")

print("""
✔ Variables store data values
✔ Python uses dynamic typing
✔ Variable names must follow rules
✔ Keywords cannot be used as variable names
✔ Use meaningful names for better readability
""")

print("========== END OF VARIABLES & NAMING RULES ==========")
