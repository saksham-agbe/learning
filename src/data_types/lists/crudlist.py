# LIST (Mutable – allows CRUD)
# Create
mylist = ["BMW","Honda", "Hyundai"]
mylist.append("Maruti")
mylist.insert(1,"Hummer")
print(mylist)

# Read
print(mylist[1]) # indexing
print(mylist[1:5]) # slicing

# Update
mylist[0] = "Ford"
print(mylist)

# Delete
mylist.remove("Hummer") 
# mylist.pop()
# del mylist[0]
# del mylist
# print(mylist)
mylist.clear
print(mylist)