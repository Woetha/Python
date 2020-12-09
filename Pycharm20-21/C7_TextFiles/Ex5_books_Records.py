# Program reads the text file in order
# The odd line contains the title of the books
# The even lines contains the author
# title -> author
with open("Files Chapter 7/books.txt") as file:
    book = file.readline()
    number = 0
    while book:
        number += 1
        for i in range(2):
            if i == 0:
                title = book.rstrip()
            else:
                author = book.rstrip()
            book = file.readline()
        print(str(number) + ".", title, "->", author)

# Shorter Version
# with open("Files Chapter 7/books.txt") as file:
# book = file.readline()
#   while book
#       author = file.readline()
#       print(book , "->", author)
#       book = file.readline()
