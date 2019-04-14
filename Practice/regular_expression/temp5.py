#console I/O

inp=input("enter a number")

number1=int(inp)

inp1=input("enter a number")
number2=int(inp1)

sum=number1+number2
print(sum)


#File I/O


inp=input("Enter a statement")
with open("textfile.txt","w") as f:
    f.write(inp)
    
inp=input("Enter a statement:")

with open("textfile.txt","a") as f:
    f.write(inp)    


with open("textfile.txt","r") as f:
    print(f.read())