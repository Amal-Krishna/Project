import re


sentence="Iron man was released in 2008"

re.match(r"[a-zA-Z]+",sentence)

sentence1="2018 saw the launch some great movies"


re.match(r"[a-zA-Z]+",sentence1)

re.search(r"[a-zA-Z]+",sentence1)


#starts

re.match(r"^2018",sentence1)

if re.match(r"^2018",sentence):
    print("match")
else:
    print("no match")
    
if re.match(r"^2018",sentence1):
    print("match")
else:
    print("no match")
    
    
#ends

if re.search(r"movies$",sentence):
    print("match")
else:
    print("no match")
    


if re.search(r"movies$",sentence1):
    print("match")
else:
    print("no match")