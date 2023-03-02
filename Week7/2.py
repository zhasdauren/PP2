# WRITE

# Open a file for writing purposes
# 'w: write' vs 'a: append' mode

#f = open('output.txt', 'w')    # write overwrites the contents
f = open('output.txt', 'a') # append to the end
f.write('Another text added\n')

f.close()

f = open('output.txt', 'r')
print(f.read())
f.close()
