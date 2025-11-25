set1 = {"Haryana", "Rajasthan", "Uttrakhand"}
set2 = {"Chandigarh","Jaipur","Dehradun"}
set3 = set1.union(set2)
print(set3)


set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1 | set2 | set3 |set4
print(myset)

set = {"a","b","c"}
tuple = (1 , 2 , 3)
z = set.union(tuple)
print(z)

