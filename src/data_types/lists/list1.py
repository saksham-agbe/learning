fruits = ["Apple", "Mango", "Banana", "Cherry", "Kiwi"]
list = []

for x in fruits:
    if "a" in x:
        list.append(x)
print(list)

list1 = ["India", "Russia", "Israel"]
mylist = list1[:]
print(mylist)

list1 = ["India","Rusia", "Israel", "USA"]
mylist = list1.copy()
print(mylist)

list1 = ["India", "Russia", "Israel"]
list2 = ["BMW", "Honda", "Hyundai"]
list3 = list1 + list2
print(list3)

list1 = ["India", "Russia", "Israel"]
list2 = ["BMW", "Honda", "Hyundai"]
list1.append(list2)
print(list1)

