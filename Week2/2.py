t = [1,2,3]
t2 = ['a','b','c']
t3 = [1,2.34,True,"abcdef"]

print(type(t3))
print(t3[0])
print(type(t3[0]))
print(type(t3[-1]))

t.append(10)
print(t)
"""
t.extend(t2)
print(t)
print(t2)
"""
import random
random.shuffle(t)
print(t)

t.sort()
print(t)