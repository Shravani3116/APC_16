books = ["Harry Potter", "Wings of Fire", "The Alchemist"]


book = input("Enter a book to add: ")
books.append(book)

book = input("Enter a book to search: ")

if book in books:
    print("Book found")
else:
    print("Book not found")

book = input("Enter a book to remove: ")

if book in books:
    books.remove(book)
    print("Book removed")
else:
    print("Book not found")

print("All books:", books)

print("Total books:", len(books))