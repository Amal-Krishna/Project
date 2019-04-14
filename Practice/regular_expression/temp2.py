list1= [12,12.5,"This is string"]
print(list1)


print(list1[0])


list1.append(58.9)

list1.insert(2,"This is second string")

list1.pop()

del list1[2]

list1.append(58.9)
list1.insert(3,"string 3")

print(len(list1))

print(type(list1[2]))

for index in range(0,len(list1)):
    print(list1[index])



for item in list1:
    print(item)

list2=[12,12.5,"This is string","string 3",58.9]

for index in range(0,len(list2)):
    list2[index]=45    