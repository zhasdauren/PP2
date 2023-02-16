'''
int square(int x){
    return x * x;
}
cout << square(3);
'''
# void function, non-friutful function
def square(x):
    print(x * x)

# fruitful function
def squareReturn(x):
    return (x * x)
'''
a = int(input())
#x = square(a) # return nothing => None => NoneType
x = squareReturn(a)
print(x + 10)
'''
def sum2(x,y):
    return x + y

def sum3(x,y,z):
    return x + y + z

def mySum(*x):
    print(type(x))
    #return sum(x)
    s = 0
    for i in x:
        s += i
    return s

a, b, c = 10, 5, 7
print(a)
print(b)
print(sum2(a,b))

print(mySum(1,2,3,4,5,10,234,324,7,234,-2))