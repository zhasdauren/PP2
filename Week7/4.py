# DELETE

# Delete a file
import os   # Operating System

# try:
#     os.remove('new.txt')
# except:
#     print('Such a file does not exist')

# print('Enter another file name')

#   Check if exists first
if os.path.exists('new.txt'):
    os.remove('new.txt')
else:
    print('Such a file does not exist')



# Create a folder
#os.mkdir('tmp')
#print('Created a folder')

t = os.listdir()
print(t)
print(type(t))
print(len(t))

path = os.getcwd()

os.chdir('tmp')
print(os.getcwd())
files = os.listdir()
print(files)
print(type(files))
print(len(files))

for file in files:
    os.remove(file)

files = os.listdir()
print(len(files))

os.chdir(path)
print(os.getcwd())

# Delete a folder
os.rmdir('tmp')    # Make sure it is EMPTY!
print('Deleted a folder')