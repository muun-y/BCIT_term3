from catalogue import Catalogue
from libraryMenu import LibraryMenu


class Library:
    """
    A class representing a library.

    Attributes:
    - catalogue (Catalogue): The catalogue of library items.

    Methods:
    - check_out(call_number): Checks out an item from the library based on its call number.
    - return_item(call_number): Returns an item to the library based on its call number.
    - display_available_books(): Displays available books in the library.
    - library_run(): Runs the library menu.
    """

    def __init__(self):
        """
        Initialize a Library object with an empty catalogue.
        """
        self.catalogue = Catalogue()
        self.menu = LibraryMenu()

    def check_out(self, call_number):
        """
        Checks out an item from the library based on its call number.

        Args:
        - call_number (str): The call number of the item to be checked out.
        """
        for item in self.catalogue.item_list:
            if item.call_number == call_number:
                if item.check_availability():
                    item.num_of_copies -= 1
                    print(
                        f"Book with call number {call_number} checked out successfully.")
                    return
                else:
                    print(
                        f"Book with call number {call_number} is not available for check out.")
                    return
        print(f"Book with call number {call_number} not found.")

    def return_item(self, call_number):
        """
        Returns an item to the library based on its call number.

        Args:
        - call_number (str): The call number of the item to be returned.
        """
        for item in self.catalogue.item_list:
            if item.call_number == call_number:
                item.num_of_copies += 1
                print(
                    f"Book with call number {call_number} returned successfully.")
                return
        print(f"Book with call number {call_number} not found.")

    def display_available_books(self):
        """
        Displays available books in the library.
        """
        if not self.catalogue.item_list:
            print("No books available.")
        else:
            for book in self.catalogue.item_list:
                print("\n" + str(book))

    def library_run(self):
        while True:
            self.menu.display_menu()
            choice = input("Enter your choice: ")

            if choice == "1":
                # Add a book
                self.catalogue.add_item()
            elif choice == "2":
                # Display available books
                self.display_available_books()
            elif choice == "3":
                # Find books by title
                title = input(
                    "Enter the title of the book to find: ")
                self.catalogue.find_items(title)
            elif choice == "4":
                # Check out a book
                call_number = input(
                    "Enter the call number of the book to check out: ")
                self.check_out(call_number)
            elif choice == "5":
                # Return a book
                call_number = input(
                    "Enter the call number of the book to return: ")
                self.return_item(call_number)
            elif choice == "6":
                # Remove a book
                call_number = input(
                    "Enter the call number of the book to check out: ")
                self.catalogue.remove_item(call_number)
            elif choice == "7":
                # Exit
                print("Exiting the library.")
                break
            else:
                print("Invalid choice. Please enter a number from 1 to 7.")
