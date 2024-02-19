class Library:
    def __init__(self, filename="books.txt"):
        self.filename = filename
        self.file = open(self.filename, "a+")  # Open file in "a+" mode to read and append

    def __del__(self):
        self.file.close()  # Close the file when the object is destroyed

    def list_books(self):
        # Read the contents of the file
        self.file.seek(0)  # Move the file cursor to the beginning
        lines = self.file.read().splitlines()

        if not lines:
            print("No books found in the library.")
            return



        print("List of books:")
        for line in lines:
            book_info = line.strip().split(",")  # Split the line into book attributes
            book_title = book_info[0]
            book_author = book_info[1].capitalize()  # Capitalize the first letter of author's name
            print(f"Book: {book_title}, Author: {book_author}")

    def add_book(self):
        # Ask user input for book details
        while True:
            book_title = input("Enter the title of the book: ")
            if any(c.isalnum() for c in book_title):
                break
            else:
                print("Invalid input. Please enter the title using letters and/or numbers.")

        while True:
            author_name = input("Enter the author's name: ")
            if all(part.isalpha() for part in author_name.split()):
                break
            else:
                print("Invalid input. Please enter the author's name using letters only.")

        # Capitalize first and last name
        author_name = ' '.join(part.capitalize() for part in author_name.split())

        # Validate release year
        while True:
            release_year = input("Enter the release year of the book: ")
            if release_year.isdigit() and 99 < int(release_year) <= 2024 and len(release_year) <= 4:
                break
            else:
                print("Invalid input. Please enter a valid year smaller or equal to 2024 and greater than 99.")

        # Validate number of pages
        while True:
            num_pages = input("Enter the number of pages in the book: ")
            if num_pages.isdigit() and int(num_pages) > 0 and int(num_pages) <= 10003:
                break
            else:
                print(
                    "Invalid input. Please enter a valid number of pages greater than 0 and less than or equal to 10,003.")

        # Create a string with book information
        book_info = f"{book_title},{author_name},{release_year},{num_pages}\n"

        # Append the book information to the file
        self.file.write(book_info)
        print("Book added successfully.")

    def remove_book(self):
        # Ask user input for book title to be removed
        book_title = input("Enter the title of the book you want to remove: ")


        self.file.seek(0)
        lines = self.file.read().splitlines()

        if not lines:
            print("No books found in the library.")
            return


        for line in lines:
            book_info = line.strip().split(",")
            if book_info[0] == book_title:
                lines.remove(line)
                break
        else:
            print(f"Book with title '{book_title}' not found in the library.")
            return


        self.file.seek(0)
        self.file.truncate()


        for line in lines:
            self.file.write(line + '\n')

        print(f"Book '{book_title}' removed successfully.")


# Define the menu function
def menu():
    print("*** MENU ***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("4) Exit")
    choice = input("Enter your choice (1, 2, 3, or 4): ")

    if choice == "1":
        lib.list_books()
    elif choice == "2":
        while True:
            lib.add_book()
            continue_choice = input("Do you want to add another book? (yes/no): ")
            if continue_choice.lower() != "yes":
                break
    elif choice == "3":
        lib.remove_book()
    elif choice == "4":
        print("Exiting the program.")
        exit()
    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")



lib = Library()


while True:
    menu()

