from libraryItem import LibraryItem


class Book(LibraryItem):
    """
    A class representing a book in the library.

    Attributes:
        title (str): The title of the book.
        call_number (str): The call number assigned to the book.
        author (str): The author of the book.
        num_of_copies (int): The number of copies available in the library.
    """

    def __init__(self, author, title, call_number, num_of_copies):
        """
        Initializes a Book object with the given title, call number, author, and number of copies.

        Args:
            title (str): The title of the book.
            call_number (str): The call number assigned to the book.
            author (str): The author of the book.
            num_of_copies (int): The number of copies available in the library.
        """
        super().__init__(title, call_number, num_of_copies)
        self.author = author

    def __str__(self):
        """
        Returns a string representation of the book.

        Returns:
            str: A string containing the book's title, call number, author, and available copies.
        """
        return "\n".join([
            f"{key.capitalize()}: {value}" for key, value in self.__dict__.items()]
        )


class Journal(LibraryItem):
    """
    A class representing a journal in the library.

    Attributes:
        title (str): The title of the journal.
        author (str): The author of the journal.
        issue_number (str): The issue number of the journal.
        publisher (str): The publisher of the journal.
        call_number (str): The call number assigned to the journal.
        num_of_copies (int): The number of copies available in the library.
    """

    def __init__(self, title, author, issue_number, publisher, call_number, num_of_copies):
        """
        Initializes a Journal object with the given title, author, issue number, publisher,
        call number, and number of copies.

        Args:
            title (str): The title of the journal.
            author (str): The author of the journal.
            issue_number (str): The issue number of the journal.
            publisher (str): The publisher of the journal.
            call_number (str): The call number assigned to the journal.
            num_of_copies (int): The number of copies available in the library.
        """
        super().__init__(title, call_number, num_of_copies)
        self.author = author
        self.issue_number = issue_number
        self.publisher = publisher

    def __str__(self):
        """
        Returns a string representation of the journal.

        Returns:
            str: A string containing the journal's title, author, issue number, publisher, and available copies.
        """
        return "\n".join([
            f"{key.capitalize()}: {value}" for key, value in self.__dict__.items()]
        )


class DVD(LibraryItem):
    """
    A class representing a DVD in the library.

    Attributes:
        title (str): The title of the DVD.
        release_date (str): The release date of the DVD.
        region_code (str): The region code of the DVD.
        call_number (str): The call number assigned to the DVD.
        num_of_copies (int): The number of copies available in the library.
    """

    def __init__(self, title, release_date, region_code, call_number, num_of_copies):
        """
        Initializes a DVD object with the given title, release date, region code, call number,
        and number of copies.

        Args:
            title (str): The title of the DVD.
            release_date (str): The release date of the DVD.
            region_code (str): The region code of the DVD.
            call_number (str): The call number assigned to the DVD.
            num_of_copies (int): The number of copies available in the library.
        """
        super().__init__(title, call_number, num_of_copies)
        self.release_date = release_date
        self.region_code = region_code

    def __str__(self):
        """
        Returns a string representation of the DVD.

        Returns:
            str: A string containing the DVD's title, release date, region code, and available copies.
        """
        return "\n".join([
            f"{key.capitalize()}: {value}" for key, value in self.__dict__.items()]
        )
