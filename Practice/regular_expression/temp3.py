#tuple is immutable

tuple1=(12.8,147,"this is a string",15.9)

print(tuple1)

print(tuple1[2])

tuple2=("this another string",15.3,78.9)

tuple3=tuple1+tuple2
print(tuple3)


print(len(tuple2))


for index in range(0,len(tuple3)):
    print(tuple3[index])



for item in tuple2:
    print(item)