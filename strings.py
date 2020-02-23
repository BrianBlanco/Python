myString = "I like apples!"

# String length
print(len(myString))

# Index of a character on a string
print(myString.index('e'))

# Count the number of coincidences of a character
print(myString.count("p"))

# Show the characters in a range
print(myString[3:7])

# Show the characters in a range skipping 2 characters
print(myString[3:10:2])

# Reverse the string
print(myString[::-1])

# To uppercase
print(myString.upper())

# To lowercase
print(myString.lower())

# Return true if the string starts with "I like"
print(myString.startswith("I like"))

# Return true if the string ends with "!"
print(myString.endswith("!"))

# Split the string and turn it in into array
print(myString.split(" "))