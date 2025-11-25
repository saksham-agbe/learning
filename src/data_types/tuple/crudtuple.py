# TUPLE (Immutable – NO direct update or delete)

# Create

mytuple = ("India", "Israel", "Russia", "USA")

# Read
print(mytuple[1])
print(mytuple[0:3])

# Update
temp = list(mytuple)
temp[0] = "Japan"
mytuple = tuple(temp)
print(mytuple)

# Delete
del mytuple
