def mult2(a,b):
    return a * b

def mult3(a,b,c):
    return a * b * c

def mult(*args): # arbitrary number of arguments
    result = 1
    for number in args:
        result = result * number
    
    return result

print(mult(3,4,2,343,3434))

t = input().split()
print(t)
n = []
for i in t:
    n.append(int(i))

print(n)