import re

txt = 'ac cat cot car coat cut ccc abcd'

t = re.findall(r"\bc\w+t", txt)
print(t)