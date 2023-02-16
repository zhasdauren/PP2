class Library:
    def __init__(self):
        self.books = []


class Book:
    def __init__(self, name,author):
        self.name = name
    def __str__(self):
        return self.name

libraryOfKBTU = Library()
print(libraryOfKBTU)
print(libraryOfKBTU.books)

b1 = Book("Python Programming","Zhasdauren")
libraryOfKBTU.books.append(b1)
print(libraryOfKBTU.books)

for book in libraryOfKBTU.books:
    print(book)

# c1 = Car()
# print(c1)