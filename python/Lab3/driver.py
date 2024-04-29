from catalogue import Catalogue
from libraryitemgenerator import LibraryItemGenerator
from library import Library


def main():
    """Demonstrates the functionality of a library system.

    This function creates instances of a Catalogue, LibraryItemGenerator, and Library.
    It adds books, journals, and DVDs to the library catalog using the LibraryItemGenerator,
    displays the available items in the library, finds items by title, checks out an item,
    returns an item, and removes an item from the catalog.

    """
    # Create a Catalogue
    my_catalogue = Catalogue()

    # Create a LibraryItemGenerator
    item_generator = LibraryItemGenerator()

    # Create a Library with the Catalogue
    my_library = Library(my_catalogue)

    # Adding books to the library
    item_generator.add_item_to_catalogue(
        my_catalogue, "Book", "The Catcher in the Rye", "C123", "J.D. Salinger", 3
    )
    item_generator.add_item_to_catalogue(
        my_catalogue, "Book", "To Kill a Mockingbird", "M456", "Harper Lee", 5
    )

    item_generator.add_item_to_catalogue(
        my_catalogue,
        "Journal",
        "Munyoung's diary",
        "J789",
        "John Doe",
        2,
        "N123",
        "BCIT",
    )

    # Adding a DVD to the library
    item_generator.add_item_to_catalogue(
        my_catalogue, "DVD", "Lion King", "D101", 10, "2022-01-01", "Region 1"
    )

    # Display available items in the library
    my_library.display_available_items()

    # Find items by title
    found_items = my_catalogue.find_items("Lion King")
    if found_items:
        print("\nItems found:")
        for found_item in found_items:
            print(found_item)

    # Check out an item
    my_library.check_out("J789")
    my_library.display_available_items()

    # Return an item
    my_library.return_item("J789")
    my_library.display_available_items()

    # Remove an item
    my_catalogue.remove_item("D101")
    my_library.display_available_items()


if __name__ == "__main__":
    main()
