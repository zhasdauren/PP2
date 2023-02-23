import re

txt = 'absdabbbbbf asd sdabdfs abbsd sadabbb asdwoiepoqweabb'

t = re.findall('ab{2,3}', txt)
print(t)