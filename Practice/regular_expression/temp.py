print("Helllo World")

a=5
print(a)


b=["a","b","c","d","e"]
print(b)



name="justice league"
print(name[1:5])


sen="I love avengers and justice league\n"
print(sen*5)


print("justice league",end=" ")
print("avengers")


# lists and Tic Tac Toe

game= [[0, 0, 0],
       [0, 0, 0],
       [0, 0, 0],]
for row in game:
    print(row)
    
    
    
mark=85
if mark>90:
    print("Grade O")
elif mark>80:
    print("Grade E")
elif mark>70:
    print("Grade A")
elif mark >60:
    print("Grade B")
else:
    print("Failed")
    
    
    
num1=45
num2=5
if(num1%num2==0):
    print("Divisible")
else:
    print("Not Divisible")



i=1
while i<=10:
    print(i)
    i +=1
    

for  i in range(1,11):
    print(i)


for i in range(1,6):
    for j in range(1,6):
        print(j,end=" ")
    print()



for i in range(1,11):
    if i>5:
        break
    print(i)


for i in range(1,11):
    if i>4 and i<7:
        continue
    print(i)


i=1
if i==1:
    pass
else:
    pass


i=2
if i==1:
    pass
else:
    print(i)

i=3
if i==3:
    print(i)
else:
    pass




