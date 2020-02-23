class MyClass:
    variable = "variable of the class"
    
    def printSomething(self):
        print("This is a mensaje inside the class")

# We create a "instance" of the class MyClass and assign it into myObject
myObject = MyClass()
print(myObject.variable)

# We can change the value of the object variables
myObject.variable = "Brian"
print(myObject.variable)

# We can access into the object functions
myObject.printSomething()