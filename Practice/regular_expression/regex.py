#regex -sequence of characters - used for matching character sequences

import re

sentence="I like Iron Man movie launched in 2008"

re.match(r".*",sentence)

re.match(r".+",sentence)

re.match(r"[a-zA-Z]+",sentence)

sentence2=""

re.match(r"[a-zA-Z]+",sentence2)


sentence3="ab"

sentence4="a"

sentence5="abbbb"

sentence6="b"

re.match(r"ab?",sentence3)

re.match(r"ab?",sentence4)

re.match(r"ab?",sentence5)

re.match(r"ab?",sentence6)
