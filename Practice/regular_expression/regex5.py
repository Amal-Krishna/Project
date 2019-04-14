import re


X=["This is a wolf # scary",
   "welcome to the jungle #missing",
   "11322 the number to know",
   "Remeber the name s - John",
   "I     love       avengers"
   ]

for i in range(len(X)):
    X[i] = re.sub(r"\W"," ",X[i])
    X[i] = re.sub(r"\d"," ",X[i])
    X[i] = re.sub(r"\s+[a-z]\s+"," ",X[i],flags=re.I)
    X[i] = re.sub(r"\s+"," ",X[i])
    X[i] = re.sub(r"^\s+","",X[i])
    X[i] = re.sub(r"\s$","",X[i])