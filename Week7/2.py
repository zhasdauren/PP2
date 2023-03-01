# WRITE

# Open a file for writing purposes
# 'w' vs 'a' mode

f = open('output.txt', 'a')
f.write('\nNow we added more text')
f.close()

f = open('output.txt', 'r')
print(f.read())
f.close()
