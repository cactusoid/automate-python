text = input()

print(text.strip())


import re

p = re.sub(r'^\s+|\s+$', '', text)

print(p)

