# A function is a lot of code that you can call whenever you want
def my_function():
    print("This is a function")
    
# You can call functions like this
my_function()

# Functions can accept arguments
def my_function2(name, username):
    print("Hello, %s , From my_Function!, your username is %s"%(name, username))
    
my_function2("Brian", "Brian123")

# Return statement give us something, in this case, the result of a + b
def sum_two_numbers(a, b):
    return a + b

# But is only give us the value, now we have to show it in out terminal
print(sum_two_numbers(1, 2))

# We can assing the return of a function into a variable
returnValue = sum_two_numbers(4, 5)

print(returnValue)