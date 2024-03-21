from items import Book, DVD, Journal
from libraryItemFactory import LibraryItemFactory


class BookFactory(LibraryItemFactory):
    """
    A factory class for generating Book objects.

    Methods:
    - generate_item(**kwargs): Generates a Book object based on the provided keyword arguments.
    """

    def generate_item(self, **kwargs):
        return Book(**kwargs)


class JournalFactory(LibraryItemFactory):
    """
    A factory class for generating Journal objects.

    Methods:
    - generate_item(**kwargs): Generates a Journal object based on the provided keyword arguments.
    """

    def generate_item(self, **kwargs):
        return Journal(**kwargs)


class DVDFactory(LibraryItemFactory):
    """
    A factory class for generating DVD objects.

    Methods:
    - generate_item(**kwargs): Generates a DVD object based on the provided keyword arguments.
    """

    def generate_item(self, **kwargs):
        return DVD(**kwargs)
