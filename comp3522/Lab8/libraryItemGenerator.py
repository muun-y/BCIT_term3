from factory import BookFactory, JournalFactory, DVDFactory


class LibraryItemGenerator():
    """
    A factory class for generating library items such as books, journals, and DVDs.

    Attributes:
        ITEM_INPUTS (dict): A dictionary containing input fields for each item type.
    """
    ITEM_INPUTS = {
        "book": ["title", "author", "call_number", "num_of_copies"],
        "journal": ["title", "author", "issue_number", "publisher", "call_number", "num_of_copies"],
        "dvd": ["title", "release_date", "region_code", "call_number", "num_of_copies"]
    }

    def select_factory(self):
        """
        Generates library items based on user input.

        Yields:
            LibraryItem: A library item object generated based on user input.
        """
        while True:
            item_type = input(
                "\nEnter item type (book, journal, dvd) or type 'end' to go back to menu: ")
            if item_type.lower() == 'end':
                break
            elif item_type.lower() in self.ITEM_INPUTS:
                item_info = {}
                for input_field in self.ITEM_INPUTS[item_type]:
                    item_info[input_field] = input(
                        f"Enter {input_field.replace('_', ' ')}: ")
                item = self._select_factory(item_type, **item_info)
                yield item
            else:
                print(
                    "Invalid item type. Please enter 'book', 'journal', 'dvd', or 'end'.")

    def _select_factory(self, item_type, **kwargs):
        """
        Generates a specific type of library item based on the provided item type and input fields.

        Args:
            item_type (str): The type of library item to generate.
            **kwargs: Keyword arguments representing input fields for the item.

        Returns:
            LibraryItem: A library item object.
        """
        if item_type == "book":
            return BookFactory().generate_item(**kwargs)
        elif item_type == "journal":
            return JournalFactory().generate_item(**kwargs)
        elif item_type == "dvd":
            return DVDFactory().generate_item(**kwargs)
