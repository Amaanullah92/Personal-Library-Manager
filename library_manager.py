import json
import os

# File to store library data
LIBRARY_FILE = "library.txt"

# Load library from file if exists
def load_library():
    if os.path.exists(LIBRARY_FILE):
        with open(LIBRARY_FILE, "r") as file:
            return json.load(file)
    return []

# Save library to file
def save_library(library):
    with open(LIBRARY_FILE, "w") as file:
        json.dump(library, file, indent=4)

# Function to add a book
def add_book(library):
    title = input("Enter the book title: ").strip()
    author = input("Enter the author: ").strip()
    try:
        year = int(input("Enter the publication year: ").strip())
    except ValueError:
        print("Invalid year! Please enter a valid number.")
        return
    genre = input("Enter the genre: ").strip()
    read_status = input("Have you read this book? (yes/no): ").strip().lower() == "yes"

    book = {
        "Title": title,
        "Author": author,
        "Year": year,
        "Genre": genre,
        "Read": read_status
    }
    library.append(book)
    print("✅ Book added successfully!")

# Function to remove a book
def remove_book(library):
    title = input("Enter the title of the book to remove: ").strip()
    for book in library:
        if book["Title"].lower() == title.lower():
            library.remove(book)
            print("✅ Book removed successfully!")
            return
    print("❌ Book not found!")

# Function to search for a book by title or author
def search_book(library):
    print("Search by:\n1. Title\n2. Author")
    choice = input("Enter your choice: ").strip()

    if choice == "1":
        search_title = input("Enter the title: ").strip().lower()
        results = [book for book in library if search_title in book["Title"].lower()]
    elif choice == "2":
        search_author = input("Enter the author: ").strip().lower()
        results = [book for book in library if search_author in book["Author"].lower()]
    else:
        print("❌ Invalid choice!")
        return

    if results:
        print("\n📚 Matching Books:")
        for i, book in enumerate(results, 1):
            print(f"{i}. {book['Title']} by {book['Author']} ({book['Year']}) - {book['Genre']} - {'Read' if book['Read'] else 'Unread'}")
    else:
        print("❌ No matching books found.")

# Function to display all books
def display_books(library):
    if not library:
        print("📂 Your library is empty!")
        return

    print("\n📚 Your Library:")
    for i, book in enumerate(library, 1):
        print(f"{i}. {book['Title']} by {book['Author']} ({book['Year']}) - {book['Genre']} - {'Read' if book['Read'] else 'Unread'}")

# Function to display statistics
def display_statistics(library):
    total_books = len(library)
    if total_books == 0:
        print("📊 No books in the library.")
        return

    read_books = sum(1 for book in library if book["Read"])
    percentage_read = (read_books / total_books) * 100

    print(f"📊 Total books: {total_books}")
    print(f"📖 Percentage read: {percentage_read:.2f}%")

library = load_library()

while True:
    print("\n📚 Personal Library Manager")
    print("1. Add a book")
    print("2. Remove a book")
    print("3. Search for a book")
    print("4. Display all books")
    print("5. Display statistics")
    print("6. Exit")

    choice = input("Enter your choice: ").strip()

    match choice: 
        case "1":
            add_book(library)
        case "2":
            remove_book(library)
        case "3":
            search_book(library)
        case "4":
            display_books(library)
        case "5":
            display_statistics(library)
        case "6":
            save_library(library)
            print("📁 Library saved to file. Goodbye!")
            break
        case _:
            print("❌ Invalid choice! Please enter a number between 1 and 6.")