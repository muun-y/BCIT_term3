from libraryitem import LibraryItems


class Book(LibraryItems):
    """Represents a book in a library catalog.

    Attributes:
    - title (str): The title of the book.
    - call_number (str): The unique identifier of the book.
    - author (str): The author of the book.
    - num_of_copies (int): The number of available copies of the book.

    Methods:
    - __str__(): Returns a formatted string representation of the book.
    """

    def __init__(self, title, call_number, author, num_of_copies):
        """Initialize a Book instance.

        :param title (str): The title of the book.
        :param call_number (str): The unique identifier of the book.
        :param author (str): The author of the book.
        :param num_of_copies (int): The number of available copies of the book.
        """
        super().__init__(call_number, num_of_copies, title)
        self.author = author

    def __str__(self):
        """Return a formatted string representation of the book."""
        return f"Title: {self.title}\nCall Number: {self.call_number}\nAuthor: {self.author}\nAvailable Copies: {self.num_of_copies}"


class Journal(LibraryItems):
    """Represents a journal in a library catalog.

    Attributes:
    - title (str): The title of the journal.
    - call_number (str): The unique identifier of the journal.
    - author (str): The author of the journal.
    - num_of_copies (int): The number of available copies of the journal.
    - issue_number (str): The issue number of the journal.
    - publisher (str): The publisher of the journal.

    Methods:
    - __str__(): Returns a formatted string representation of the journal.
    """

    def __init__(
        self, title, call_number, author, num_of_copies, issue_number, publisher
    ):
        """Initialize a Journal instance.

        :param title (str): The title of the journal.
        :param call_number (str): The unique identifier of the journal.
        :param author (str): The author of the journal.
        :param num_of_copies (int): The number of available copies of the journal.
        :param issue_number (str): The issue number of the journal.
        :param publisher (str): The publisher of the journal.
        """
        super().__init__(call_number, num_of_copies, title)
        self.author = author
        self.issue_number = issue_number
        self.publisher = publisher

    def __str__(self):
        """Return a formatted string representation of the journal."""
        return f"Title: {self.title}\nCall Number: {self.call_number}\nAuthor: {self.author}\nAvailable Copies: {self.num_of_copies}\nIssue Number: {self.issue_number}\nPublisher: {self.publisher}"


class DVD(LibraryItems):
    """Represents a DVD in a library catalog.

    Attributes:
    - title (str): The title of the DVD.
    - call_number (str): The unique identifier of the DVD.
    - num_of_copies (int): The number of available copies of the DVD.
    - release_date (str): The release date of the DVD.
    - region_code (str): The region code of the DVD.

    Methods:
    - __str__(): Returns a formatted string representation of the DVD.
    """

    def __init__(self, title, call_number, num_of_copies, release_date, region_code):
        """Initialize a DVD instance.

        :param title (str): The title of the DVD.
        :param call_number (str): The unique identifier of the DVD.
        :param num_of_copies (int): The number of available copies of the DVD.
        :param release_date (str): The release date of the DVD.
        :param region_code (str): The region code of the DVD.
        """
        super().__init__(call_number, num_of_copies, title)
        self.release_date = release_date
        self.region_code = region_code

    def __str__(self):
        """Return a formatted string representation of the DVD."""
        return f"Title: {self.title}\nCall Number: {self.call_number}\nAvailable Copies: {self.num_of_copies}\nRelease Date: {self.release_date}\nRegion Code: {self.region_code}"
