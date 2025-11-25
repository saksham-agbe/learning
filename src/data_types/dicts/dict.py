dict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year"  : "1960",
}
print(dict)

family = {
    "Child 1":{
        "name" : "Jeorge",
        "age" : 24,
        "year" : 2002
    },
    "Child 2":{
        "name" : "Emila",
        "age" : "20" ,
        "year" : 2004
    },
    "Child 3":{
        "name" : "George",
        "age" : 30,
        "year": 2010,
    }
}
print(family)

names = ["football" , "Cricket"]
print(names[1])
for x in names:
    print(x)

#set = {"India" , 1 , {"name" : "Saksham"} , "India"}
set = ["India" , 1 , {"name" : "Saksham"} , "India"]


# countries = list(set)
print(set)

print(f"countries = {type(set[2])}")
