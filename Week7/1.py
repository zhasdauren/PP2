# READ

# Opening a file
f = open('input.txt', 'r')
print(type(f))

# Read all
#print(f.read())

# Read by characters
# print(f.read(6))
# print(f.read(6))

# # Read a line
# print(f.readline(), end=' ')
# print(f.readline(), end=' ')

# s = f.readline()
# print(s)
# print()


# Read all by lines
import re
for x in f:
    if None != re.search('[a-z]', x):
        print(x, end='')

# Close the file
f.close()