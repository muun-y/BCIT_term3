from book import Book, Journal, DVD


class LibraryItemGenerator:
    """Generates instances of library items and adds them to a catalogue.

    Methods:
    - generate_item(item_type, *args): Generates an instance of a library item based on the provided item_type.
    - add_item_to_catalogue(catalogue, item_type, *args): Generates an item and adds it to the given catalogue.
    """

    def __init__(self):
        """Initialize the LibraryItemGenerator."""
        pass

    def generate_item(self, item_type, *args):
        """Generate an instance of a library item based on the provided item_type.

        :param item_type (str): The type of library item to generate ("Book", "Journal", or "DVD").
        :param *args: Variable-length argument list containing the parameters for the specific library item type.

        :returns: LibraryItems: An instance of the generated library item.
        """
        if item_type == "Book":
            return Book(*args)
        elif item_type == "Journal":
            return Journal(*args)
        elif item_type == "DVD":
            return DVD(*args)
        else:
            raise ValueError("Invalid item type")

    def add_item_to_catalogue(self, catalogue, item_type, *args):
        """Generate an item and add it to the given catalogue.

        :param catalogue (Catalogue): The catalog where the item will be added.
        :param item_type (str): The type of library item to generate ("Book", "Journal", or "DVD").
        :param *args: Variable-length argument list containing the parameters for the specific library item type.
        """
        item_to_add = self.generate_item(item_type, *args)
        catalogue.add_item(item_to_add)
