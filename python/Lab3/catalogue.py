import difflib


class Catalogue:
    """Represents a catalog of items in a library."""

    def __init__(self):
        """
        Initialize the Catalogue.

        :return: The item_list attribute is an empty list to store items in the catalog.
        """
        self.item_list = []

    def find_items(self, string):
        """
        Find items in the catalog based on a search string.

        :param string: The search string to find items by title.
        :precondition: string must be a string.
        :return: A list of items matching the search string.

        If no items are found, suggests similar titles using difflib.
        """
        found_items = []
        for item in self.item_list:
            if string.lower() in item.title.lower():
                found_items.append(item)
        if not found_items:
            similar_titles = difflib.get_close_matches(
                string, [item.title for item in self.item_list]
            )
            if similar_titles:
                print(
                    f"Item not found. Did you mean one of these titles? {', '.join(similar_titles)}"
                )
            else:
                print("Item not found.")
        return found_items

    def add_item(self, item):
        """
        Add an item to the catalog.

        :prama item: An instance of a library item to be added.

        If the item is not already in the catalog, it is appended to the item_list.
        """
        if item not in self.item_list:
            self.item_list.append(item)

    def remove_item(self, call_number):
        """
        Remove an item from the catalog based on its call number.

        :param call_number (str): The call number of the item to be removed.
        :return: Prints a message indicating the success or failure of the removal process.
        """
        for item in self.item_list:
            if item.call_number == call_number:
                self.item_list.remove(item)
                print(f"Item with call number {call_number} removed.")
                return
        print(f"Item with call number {call_number} not found.")
