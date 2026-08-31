from books.book import add_book, display_book
from members.member import add_member, display_member
from transactions.transaction import issue_book, return_book

book = input("Enter book name: ")
member = input("Enter member name: ")

add_book(book)
display_book(book)

add_member(member)
display_member(member)

issue_book(book, member)
return_book(book, member)