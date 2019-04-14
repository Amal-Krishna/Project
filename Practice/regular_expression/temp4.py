#key - value pair

dict1={}

dict1["apple"]="apple is a fruit"
dict1["orange"]="orange is sweet"
dict1["grape"]="grapeis great"
dict1["cars"]="cars are fast"
dict1["python"]="python is a simple language"


print(dict1)


print(dict1["apple"])
print(dict1["python"])

print(dict1.get("orange"))

print(dict1.get("jython"))

print(dict1.get("bmw","value does not excist"))


print(dict1.get("cars","value does not excist"))

del dict1["orange"]

print(len(dict1))

listofkeys=list(dict1.keys())

listofvalues=list(dict1.values())


for key in dict1.keys():
    print(dict1[key])

for value in dict1.values():
    print(value)


