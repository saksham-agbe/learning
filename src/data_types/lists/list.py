mylist = ["India", "Israel", "Russia"]
print(mylist)

list1 = ["India", "Isreal", "Russia"]
print(len(list1))

list1 = ["India", "Israel", "Russia"]
print(type(list1))

thislist = ["BMW", "Hyundai", "Honda"]
if "BMW" in thislist:
    print("yes,'BMW' is present in the list")

thislist1 = ["BMW", "Hyundai", "Honda"]
print(thislist1[1])

thislist2 = ["India", "Israel", "Russia"]
thislist2[1] = "USA" 
print(thislist2)

thislist2 = ["India", "Israel", "Russia"]
thislist2.append("USA")
print(thislist2)

thislist2 = ["India", "Israel", "Russia"]
thislist2.insert(2, "USA")
print(thislist2)

list1 = ["India", "Israel", "Russia"]
list2 = ["Bmw", "Hyundai", "Honda"]
list1.extend(list2)
print(list1)

list1 = ["India", "Israel", "Russia"]
list1.clear()
print(list1)

list1 = ["India", "Israel", "Russia"]
list1.pop()
print(list1)

list1 = ["India", "Israel", "Russia"]
list1.pop(1)
print(list1)

list1 = ["India", "Israel", "Russia"]
del list1[2]
print(list1)

list1 = ["India", "Israel", "Russia"]
del list1
print(list1)


