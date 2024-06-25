# Library Management System
    
class Book:
    def __init__(self, title, author, genre, availability_status):
        self.title = title
        self.author = author
        self.genre = genre
        self.availability_status = availability_status

    def get_info(self):
        print(f"{self.title}, {self.author}, {self.genre}, {self.availability_status}")

class User:
    def __init__(self, name, library_id, borrowed_books):
        self.name = name
        self.library_id = library_id
        self.borrowed_books = borrowed_books

    def get_info(self):
        print(f"{self.name}, {self.library_id}, {self.borrowed_books}")

class Author:
    def __init__(self, name, biography):
        self.name = name
        self.biography = biography
    
    def get_info(self):
        print(f"{self.name}, {self.biography}")

books = {
    "Harry Potter": Book("Harry Potter","J.K Rowlings","Fantasy", "yes") 
}

users = {
    "user": User("Jason", "21222005012345", "Harry Potter")
}

authors = {
    "author": Author("J.K Rowlings", "Joanne Rowling was born on July 31, 1965, in Yate, near Bristol, England. She grew up in England and in Chepstow, Gwent, Wales. She loved reading and wrote her first story at the age of six. After graduating from the University of Exeter in 1986, Rowling began working for Amnesty International in London, England.")
}

def main():
    while True:
        input1 = input(''' 
                       
 Welcome to the Library Management System!
                       
1. Book Operations
2. User Operations
3. Author Operations
4. Quit
                       
 ''')
        if input1 == '1':
            book_menu()
        elif input1 == '2':
            user_menu()
        elif input1 == '3':
            author_menu()
        elif input == '4':
            print(" Thank you for using the Library Management System!")
            break
        else:
            print("Invalid input.")

def book_menu():
    while True:
        input1 = input('''
                       
Book Operations:
                       
        1. Add a new book
        2. Borrow a book
        3. Return a book
        4. Search for a book
        5. Display all books            
        6. Quit
                       
''')
        
        if input1 == "1":
            add()
        elif input1 == "2":
            borrow()
        elif input1 == "3":
            return_book()
        elif input1 == "4":
            search()
        elif input1 == "5":
            print("All books:")
            display_books()
        elif input1 == "6":
            return main()
        else:
            print("Invalid input")
            break

def display_books():
    for key in books.keys():
        books[key].get_info()

def search():
    while True:
        book = input("Please enter the name of the book you want to search for: \n").title()
        if book in books.keys():
            books[book].get_info()
            return
        
        else:
            print(f"{book} is not in the Library, Please try again")
            return
    
def add():
    while True:
        add_title = input("Please enter the title of the book you would like to add to the Library: \n").title()
        add_author = input("Please enter the author of the book would like to add:\n").title()
        add_genre = input("Please enter the genre of the book you would like to add to the Library:\n").title()
        books[add_title] = Book(add_title, add_author, add_genre,"yes")
        print(f"{add_title} by {add_author} has been added to the Library")
        return
        
def borrow():
    while True:
        book = input("Please enter the title of the book you would like to borrow:\n")
        if book in books:
            if books[book].availability_status == "yes":
                books[book].availability_status = "no"
                print(f"{book} has been borrowed from the Library!")
                return
        elif books[book].availability_status == "no":
            print(f"{book} has already been borrowed, come back and check at a later date.")
            return
    
def return_book():
    while True:
        returned = input("Please enter the title of the book you are returning:\n")
        if returned in books:
            if books[returned].availability_status == "no":
                books[returned].availability_status = "yes"


def user_menu():
    while True:
        input1 = input('''
           
User Operations:
                       
        1. Add a new user
        2. View user details
        3. Display all users
        4. Quit
                       
''')
        if input1 == "1":
            add_user()
        elif input1 == "2":
            view()
        elif input1 == "3":
           print("All Users:")
           display_users()
        elif input1 == "4":
            return main()
        else:
            print("Invalid input")
            break

def display_users():
    for key in users.keys():
        users[key].get_info()

def add_user():
    while True:
        add_name = input("Please enter the name of the user you would like to add:\n").title()
        add_library_id = input("Please enter the library id of the user you would like to add:\n").title()
        add_borrowed_books = input("Please enter the borrowed books:\n").title()
        users[add_name] = User(add_name, add_library_id, add_borrowed_books)
        print(f"User {add_name}, library id number {add_library_id} has borrowed {add_borrowed_books} from the Library.")
        return

def view():
    user_input = input("Please enter the name of the user that you would like to view details for:\n")
    if user_input in users:
         user = users[user_input]
         print(f"User Name: {user.name}")
         print(f"Library ID: {user.library_id}")
         print(f"Borrowed Books: {user.borrowed_books}")
    else:
        print("User not found")

def author_menu():
    while True:
        input1 = input('''
                       
 Author Operations:
                       
        1. Add a new author
        2. View author details
        3. Display all authors
        4. Quit
                       
''')
        if input1 == "1":
            add_author()
        elif input1 == "2":
            view_author()
        elif input1 == "3":
            display_authors()
        elif input1 == "4":
            return main()
        else:
            print("Invalid input")
            break

def display_authors():
    for key in authors.keys():
        authors[key].get_info()

def add_author():
    while True:
        add_name = input("Please enter the name of the author you would like to add:\n").title()
        add_biography = input("Please enter the biography of the author you would like to add:\n").title()
        authors[add_name] = Author(add_name, add_biography)
        print(f"Author: {add_name}'s biography is: {add_biography}")
        return

def view_author():
    author_input = input("Please enter the name of the author that you would like to view details for:\n")
    if author_input in authors:
        author = authors[author_input]
        print(f"Author name: {author.name}")
        print(f"Biography: {author.biography}")
    else:
        print("Author nor found")
   
main()