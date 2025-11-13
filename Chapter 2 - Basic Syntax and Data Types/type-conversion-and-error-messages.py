# Convert between types with built-in functions:
# int(), float(), str(), bool()
num_str = "123"
print(type(num_str))
num = int(num_str)
print(type(num))

pi_float = '3.14'
print(type(pi_float))
pi = float(pi_float)
print(type(pi))

# Common errors
# num_abc = int("abc") # ValueError: invalid literal for int() with base 10: 'abc'
# print(undeclared) # NameError: name 'undeclared' is not defined
