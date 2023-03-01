# READ

# Opening a file
f = open('input.txt')

# Read all
#print(f.read(6))

# Read by characters

# Read a line
#print(f.readline())

# Read all by lines
for x in f:
    print(x)

# Close the file
f.close()