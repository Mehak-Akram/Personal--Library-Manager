import json

FILENAME_JSON = "library.json"
FILENAME_TXT = "library.txt"

def load_library():
    try:
        with open(FILENAME_JSON, "r") as file:
            library = json.load(file)
            save_to_text_file(library)
            return library
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_library(library):
    with open(FILENAME_JSON, "w") as file:
        json.dump(library, file, indent=4)
    save_to_text_file(library)

def save_to_text_file(library):
    with open(FILENAME_TXT, "w") as file:
        if not library:
            file.write("No books in the library.\n")
        else:
            for book in library:
                file.write(f"{book['title']} - {book['author']} ({book['year']}) [{book['genre']}] Read: {'Yes' if book['read'] else 'No'}\n")

def add_book(library):
    print("\n📚 Adding a new book...")
    book = {
        "title": input("📖 Enter book title: "),
        "author": input("✍️ Enter author: "),
        "year": input("📅 Enter publication year: "),
        "genre": input("📂 Enter genre: "),
        "read": input("✅ Have you read this book? (yes/no): ").strip().lower() == "yes"
    }
    library.append(book)
    save_library(library)
    print("🎉 Book added successfully!")

def remove_book(library):
    print("\n🗑 Removing a book...")
    title = input("❌ Enter title of the book to remove: ")
    library[:] = [book for book in library if book["title"].lower() != title.lower()]
    save_library(library)
    print("✅ Book removed successfully!")

def search_book(library):
    print("\n🔎 Searching for a book...")
    title = input("📖 Enter book title to search: ")
    found_books = [book for book in library if title.lower() in book["title"].lower()]
    if found_books:
        for book in found_books:
            print(f"📖 {book['title']}, ✍️ {book['author']}, 📅 {book['year']}, 📂 {book['genre']}, ✅ Read: {'Yes' if book['read'] else 'No'}")
    else:
        print("⚠️ No books found with that title.")

def list_books(library):
    print("\n📚 Listing all books...")
    if not library:
        print("⚠️ No books in the library.")
    else:
        for book in library:
            print(f"📖 {book['title']}, ✍️ {book['author']}, 📅 {book['year']}, 📂 {book['genre']}, ✅ Read: {'Yes' if book['read'] else 'No'}")

def mark_as_read(library):
    print("\n✅ Marking a book as read...")
    title = input("📖 Enter title of the book to mark as read: ")
    for book in library:
        if book["title"].lower() == title.lower():
            book["read"] = True
            save_library(library)
            print("🎉 Book marked as read!")
            return
    print("⚠️ Book not found.")

def show_statistics(library):
    print("\n📊 Library Statistics:")
    total_books = len(library)
    read_books = sum(1 for book in library if book["read"])
    unread_books = total_books - read_books
    genres = {book["genre"] for book in library}
    print(f"📚 Total books: {total_books}\n✅ Read books: {read_books}\n📕 Unread books: {unread_books}\n📂 Genres: {', '.join(genres) if genres else 'None'}")

def menu():
    library = load_library()
    while True:
        print("\n📖 Personal Library Manager")
        print("1️⃣  Add Book\n2️⃣  Remove Book\n3️⃣  Search Book\n4️⃣  List Books\n5️⃣  Mark Book as Read\n6️⃣  Show Statistics\n7️⃣  Exit")
        choice = input("🔢 Enter your choice: ")
        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_book(library)
        elif choice == "4":
            list_books(library)
        elif choice == "5":
            mark_as_read(library)
        elif choice == "6":
            show_statistics(library)
        elif choice == "7":
            print("👋 Exiting... Have a great day!")
            save_library(library)
            break
        else:
            print("⚠️ Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
