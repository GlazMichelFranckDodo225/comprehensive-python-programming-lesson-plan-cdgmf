"""
Variables store values in memory.
Python automatically assigns a type to each variable based on its value.
"""
name = "Alice"
age = 25

print(type(name)) # str
print(type(age)) # str

"""
Variable Naming Rules
    - Cannot begin with a number .
    - Must begin with a letter or an underscore (_).
    - Can contain:
        o letters,
        o numbers,
        o underscores.
    - Case-sensitive : Name ≠ name.
    - Avoid special caraters and reserved keywords:
        o if,
        o class,
        o for,
        o etc...
"""
# Good names
user_name = "Mike"
age2 = 17
_temp = 2

# Bad names
# 2user = "John"
# class
# first - name = "Hugo"