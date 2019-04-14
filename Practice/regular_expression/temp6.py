def functionName(arg1,arg2):
    print("function returns:",arg1,":",arg2)

functionName("This number is",12)

def sum(num1,num2):
    return(num1+num2)

sum(15,17)
print(sum(15,17))

def length(l):
    count=0
    for item in l:
        count +=1
    return count


length([12.5,"string",45,78.9])

list1=["string","count",15.5,78.9,48.3]

length(list1)