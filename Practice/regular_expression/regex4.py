import re

sentence1="Welcome to the year 2019"
sentence2="Just ^#@%$*&++++----- arrived at Jack's place. #fun"
sentence3="I             Love              Avengers"


sent1_mod=re.sub(r"\d","*",sentence1)


sent2_mod=re.sub(r"[@#$%^&+*-\.\']"," ",sentence2)

sent2_mod1=re.sub(r"\w"," ",sentence2)

sent2_mod2=re.sub(r"\W"," ",sentence2)

sent2_mod3=re.sub(r"[a-zA-Z]\s[a-zA-Z]","'s",sent2_mod2)


sent2_mod4=re.sub(r"\s+","'s",sent2_mod2) 


sent2_mod4=re.sub(r"\s+"," ",sent2_mod2)    


sent2_mod5=re.sub(r"\s+[a-zA-Z]\s+","'s",sent2_mod2)


sent2_mod6=re.sub(r"\s+[a-zA-Z]\s+","'s",sent2_mod4)



sent2_mod7=re.sub(r"\s[a-zA-Z]\s","'s",sent2_mod4)



sent2_mod7=re.sub(r"\s[a-zA-Z]\s"," ",sent2_mod4)

sent3_mod=re.sub(r"\s+"," ",sentence3)

sent3_mod1=re.sub(r"\s+Love\s+"," hate ",sentence3)





