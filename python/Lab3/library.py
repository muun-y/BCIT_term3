class Library:
    """Represents a library with a catalog of items."""

    def __init__(self, catalogue):
        """
        Initialize the Library.

        Parameters:
        - catalogue (Catalogue): The catalog of items in the library.
        """
        self.catalogue = catalogue

    def check_out(self, call_number):
        """
        Check out an item from the library.

        Parameters:
        - call_number (str): The call number of the item.

        Prints a message indicating the success or failure of the check-out process.
        """
        for item in self.catalogue.item_list:
            if item.call_number == call_number:
                if item.check_availability():
                    item.num_of_copies -= 1
                    print(
                        f"Item with call number {call_number} checked out successfully."
                    )
                    return
                else:
                    print(
                        f"Item with call number {call_number} is not available for check out."
                    )
                    return
        print(f"Item with call number {call_number} not found.")

    def return_item(self, call_number):
        """
        Return an item to the library.

        :param call_number: The call number of the item in String type.
        :return: Prints a message indicating the success or failure of the return process.
        """
        for item in self.catalogue.item_list:
            if item.call_number == call_number:
                item.num_of_copies += 1
                print(f"Item with call number {call_number} returned successfully.")
                return
        print(f"Item with call number {call_number} not found.")

    def display_available_items(self):
        """Display information about available items in the library."""
        if not self.catalogue.item_list:
            print("No items available.")
        else:
            for item in self.catalogue.item_list:
                print("\n" + str(item))
