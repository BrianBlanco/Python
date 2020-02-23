value1 = True
value2 = False

name = "Brian"
nameList = ["Brian", "Jose", "Pedro"]

# If the condition is true, do the following instruction
if value1:
    print("value1 is true")

# Logical gates
# AND
if value1 and value2:
    print("Both are true")

# OR
if value1 or value2:
    print("None is true")

# Return True if the name "Brian" exists in the array
if name in nameList:
    print("Brian exists in the array")

# If the first statement is false, do the code following else statement
if value1:
    print("value1 is true")
else:
    print("value1 is false")
    
# The operator "is" compare the instance of the object
# Only return true is the object is the same
x = [1,2,3]
y = [1,2,3]
print(x == y) # Prints out True
print(x is y) # Prints out False

# The operator "not" return the opposite of the following code
print(not False)
print(not True)