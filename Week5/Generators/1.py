# Iterators


# Iterables
t = (1,2,3)
for i in t:
    print(i)

# create a set
s = {45,3,45,435,43,54,53,3}
it = iter(s)
print(next(it))
print(next(it))
print(next(it))

for i in s:
    print(i, end=' ')

print()
for i in s:
    print(i, end=' ')

print()


# Creating an Iterable class


# Generators
def simple():  
    for i in range(10):  
        if(i%2==0): 
            yield i 
            #print(i, end=' ')

print(type(simple()))

for i in simple():
    print(i, end=' ')

print()
g = simple()
print(next(g))

# Generator functions


# Generator expressions

# list comprehension
list = [1,2,3,4,5,6,7]

z = [x**3 for x in list]
print(z)

# Generator expression
g = (x**3 for x in list)
print(g)

for i in g:
    print(i, end=' ')