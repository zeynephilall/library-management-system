class Library:
    def __init__(self):
        self.file_path = "books.txt"
        self.file = open(self.file_path, "a+")

    def __del__(self):
        self.file.close()

    def list_books(self):
        self.file.seek(0)
        book_lines = self.file.read().splitlines()
        if not book_lines:
            return "List is empty"
        for line in book_lines:
            book_info = line.split(',')
            return f"Book: {book_info[0]}, Author: {book_info[1]}"

    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        release_date = input("Enter release date: ")
        num_pages = input("Enter number of pages: ")
        book_info = f"{title},{author},{release_date},{num_pages}\n"
        self.file.write(book_info)

    def remove_book(self):
        title_to_remove = input("Enter the title of the book to remove: ")
        self.file.seek(0)
        book_lines = self.file.read().splitlines()
        if any(title_to_remove in line for line in book_lines):
            updated_books = [line for line in book_lines if title_to_remove not in line]
            self.file.truncate(0)
            self.file.seek(0)
            self.file.writelines("\n".join(updated_books))
            print(f"The book '{title_to_remove}' has been removed.")
        else:
            print(f"The book '{title_to_remove}' does not exist in the library.")

lib = Library()

while True:
    print("\n* MENU *")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("Q) Quit")

    user_choice = input("Enter your choice (1, 2, 3, Q): ")

    if user_choice == '1':
        print(lib.list_books())
    elif user_choice == '2':
        lib.add_book()
    elif user_choice == '3':
        lib.remove_book()
    elif user_choice.upper() == 'Q':
        print("Exiting.")
        break
    else:
        print("Invalid choice. Please enter 1, 2, 3, or Q.")