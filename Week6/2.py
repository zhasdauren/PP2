import re

txt = 'asd abb wejkwe abbbsds sdabb sfdsf'

t = re.findall('a[b]{2,3}', txt)
t2 = re.findall('abb|abbb', txt)
print(t)
print(t2)