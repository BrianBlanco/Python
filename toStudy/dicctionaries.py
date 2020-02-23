# A dicctionarie is a variable that has other variables with theis values inside
# There is two ways to create a dicctionarie

# Way 1, if you want to instantiace now but put it variables inside later
phonebook = {}

phonebook["Brian"] = 601235566
phonebook["Jose"] = 601236655
phonebook["Pedro"] = 6012358985

print(phonebook)

# Way 2,  if you create it with all the variables inside when you instantiate it
phonebook = {
    "Brian": 601235566,
    "Jose": 601236655,
    "Pedro": 6012358985
}

print(phonebook)

# How to iterate them

for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))

# How to delete one value, you have to select the variable by the name
del phonebook["Brian"]
print(phonebook)

# Or

phonebook.pop("John")
print(phonebook)