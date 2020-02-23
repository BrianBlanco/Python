numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# For each number in numbers print a number in order
for number in numbers:
    print(number)

# Print a number for each number in that range
for x in range(1, 10):
    print(x)

# Print a number for each number in that range every two
for x in range(1, 10, 2):
    print(x)

# Do the loop while the condition is True
count = 0
while count < 10:
    print(count)
    count += 1

# Break statement stop and exit the loop
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

# Continue statement continue the loop before the Break
for x in range(10):
    # Check if x is even
    if x % 2 == 0:
        continue
    print(x)

# You can use else clause for loops
count=0
while(count<5):
    print(count)
    count +=1
else:
    print("count value reached %d" %(count))
