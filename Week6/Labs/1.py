import re

txt = 'sdf asd sdabdfs abbsd sadabbb asdwoiepoqwe'

t = re.findall('ab*', txt)
print(t)