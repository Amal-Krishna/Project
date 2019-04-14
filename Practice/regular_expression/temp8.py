#list comprehension 

numbers=[1,2,3,4,5,6,7,8,9,10]

newNumbers=[]
for number in numbers:
    newNumbers.append(number)


newNumbers


newNumbers2=[number for number in numbers]

newNumbers3=[number for number in numbers if number<=5]

newNumbers4=[number for number in numbers if number%2==1]

numbers2=[1,3,5,7,9]

newNumbers5=[number for number in numbers if number not in numbers2]
    
newNumbers6=[number*2 for number in numbers]
newNumbers7=[number+5 for number in numbers]


newNumbers8=[number for number in numbers if number>3 and number<9]


#generator comprehension

squaregen=(number**2 for number in numbers)

list(squaregen)

cubegen=(number**3 for number in numbers)
list(cubegen)


mydict={"apple":5,"orange":10,"banana":15,"grape":20}
newdict={key:mydict[key] for key in mydict.keys()}
newdict2={key:mydict[key] for key in mydict.keys() if mydict[key]>10}

words=["I","like","avengers"]
sentence=" ".join(words)
sentence1=".".join(words)














