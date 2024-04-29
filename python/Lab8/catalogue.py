import difflib
from libraryItemGenerator import LibraryItemGenerator


class Catalogue:
    """
    A class representing a catalogue of library items.

    Attributes:
        item_list (list): A list containing the items in the catalogue.
        library_item_factory (object): An instance of the factory class for generating library items.

    Methods:
        find_items(string): Finds items in the catalogue based on a search string.
        add_item(): Adds a new item to the catalogue.
        remove_item(call_number): Removes an item from the catalogue based on its call number.
    """

    def __init__(self):
        """
        Initialize a Catalogue object with an empty item list.
        """
        # Using a list to store items in the catalogue
        self.item_list = []

    def find_items(self, string):
        """
        Finds library items whose titles contain the specified string.

        Args:
            string (str): The string to search for in the titles of library items.

        Returns:
            list: A list of library items whose titles contain the specified string.

        Notes:
            If no items are found matching the string exactly, the function attempts to find similar titles
            using difflib.get_close_matches and suggests them as alternatives.
        """
        # Using list comprehension to find items that match the string
        found_items = [
            item for item in self.item_list if string.lower() in item.title.lower()]

        if not found_items:
            # Using difflib.get_close_matches to find similar titles
            similar_titles = difflib.get_close_matches(
                string, [item.title for item in self.item_list])
            if similar_titles:
                print(
                    f"Book not found. Did you mean one of these titles? {', '.join(similar_titles)}")
            else:
                print("Book not found.")

        return found_items

    def add_item(self):
        """
        Adds a new item to the catalogue.
        """
        libraryItemGenerator = LibraryItemGenerator()
        for item in libraryItemGenerator.select_factory():
            if item not in self.item_list:
                self.item_list.append(item)

    def remove_item(self, call_number):
        """
        Removes an item from the catalogue based on its call number.

        Args:
        - call_number (str): The call number of the item to be removed.
        """
        for item in self.item_list:
            if item.call_number == call_number:
                # Removing the item from the list
                self.item_list.remove(item)
                print(f"Book with call number {call_number} removed.")
                return
        print(f"Book with call number {call_number} not found.")
