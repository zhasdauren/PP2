t = [1,2,3]
# for(int i=0;i<10;i++)
# for i:arr

for i in t:
    print(i*i)

print(i)

for i in range(5,20,2):
    print(i,end=' ')


t5 = list()
print(type(t5))
print(t5)

t5.append(5)
print(t5)
t5.append([6,7,8])
print(t5)

print(len(t5))
print(len(t5[1]))

t5[0] = 33
print(t5)
