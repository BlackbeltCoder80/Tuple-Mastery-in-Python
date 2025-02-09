#2. Python Data Structure Challenges in Real-World Scenarios
#Task 1: Library System Enhancement Sharpen your skills in managing and modifying data within tuples and lists.

#Problem Statement: You are maintaining a library system where each book is stored as a tuple within a list. 
# Your task is to update this system by adding new books and ensuring no duplicates.

#Existing Library Data:
from tabulate import tabulate
library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]
#- Add functionality to insert new books into `library`. Ensure that adding a duplicate book is handled appropriately.

user_UI = [[" 1. Search by Author"],
           [" 2. Add Book"],
           [" 3. Temple Collection"],
           [" 4. Exit Library"]]

def view_library_menu():
    print(tabulate(user_UI,tablefmt="grid"))

def search_library():
    pass


# Adding book functions
def add_book():
    new_book = input("Please enter the title of the book.: ")
    author_book = input("Please enter the author of book.:")
    if not new_book or not author_book:
        print("Both title and author are required!")
        return
    if new_book and author_book in library:
        print(f" The book {new_book}, {author_book} already exist in our library!")    
    if new_book and author_book not in library:
        library.append((new_book, author_book))
        print(tabulate([(new_book, author_book)],headers=["Book", "Author"], tablefmt="grid"))
        print("This book has been added Successfully")
    

# Main Loop

while True:
    view_library_menu()
    choice = input("\n Please an option.")
    if choice == "1":
        search_library()
    elif choice == "2":
        add_book()
    elif choice == "3":
        print("\n Library Collection")
        print(tabulate(library, headers=["Book", "Author"], tablefmt="grid"))
    elif choice == "4":
        print("Thank you for visiting the ""Coding Temple Video Library""")
        break
    else:
        print("Please Enter a number between 1-3")



