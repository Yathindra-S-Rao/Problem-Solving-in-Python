file = open("Books.txt", "r")

for book in file.readlines():
    if book.startswith('H'):
        print(book)

file.close()