import re

sentence="I love Avengers"

print(re.sub(r"Avengers","Justice league",sentence))

sentence1="I love Avengers Avengers"

print(re.sub(r"Avengers","Justice league",sentence1))


sentence2="I love Avengers avengers"

print(re.sub(r"Avengers","Justice league",sentence2))


sentence3="I love Avengers avengers"

print(re.sub(r"avengers","Justice league",sentence3))



sentence4="I love Avengers avengers"

print(re.sub(r"[a-z]","0",sentence4))


sentence5="I love Avengers avengers"

print(re.sub(r"[a-z]","0",sentence5,flags=re.I))


sentence6="I love Avengers avengers"

print(re.sub(r"[a-z]","0",sentence,5,flags=re.I))


print(re.sub(r"[a-z]","0",sentence,5))