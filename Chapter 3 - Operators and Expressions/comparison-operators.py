# Comparison Operators
# ==, !=, <, <=, >, >=.

# "==" Operator : Compare values directly (not types)
# print(type(3)) # int
# print(type(3.0)) # float
# boolNum = 3 == 3.0
# print(f"boolNum : {boolNum}") # True
# print(type("john"))
# print(type("JOHN"))
# boolStringComparison = "john" == "JOHN"
# print(f"boolStringComparison : {boolStringComparison}") # Case sensitivity

# "!=" Operator : test object identity, not value equality (keep distinct from ==)
# print(f"boolChain == boolNum : {boolChain == boolNum}") # True
num1 = 4
num2 = "4"
num3 = 4.0
print(f"num1 == num2 : {num1 == num2}")
print(f"num1 == num3 : {num1 == num3}")
print(f"num2 == num3 : {num2 == num3}")

# Chaining is allowed: a < b < c ==> (a < b) and (b < c)
boolChain = 1 < 2 < 4
print(f"boolChain : {boolChain}") # True

# Strings compare lexicographically
boolStr1 = "Abe" < "Ben"
print(f"boolStr1 : {boolStr1}")  # True (lexicographic)
boolStr2 = "John" > "Doe"
print(f"boolStr2 : {boolStr2}")
