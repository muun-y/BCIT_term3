import abc


class LibraryItem(abc.ABC):
    """
    Abstract class representing a library item.

    Attributes:
    - title (str): The title of the item.
    - call_number (str): The call number of the item.
    - num_of_copies (int): The number of copies available for the item.

    Methods:
    - check_availability(): Checks if the item is available for checkout.
    - __str__(): Abstract method to return a string representation of the item.
    """

    def __init__(self, *args):
        """
        Initialize a LibraryItem object with the given title, call number, and number of copies.

        Args:
        - title (str): The title of the item.
        - call_number (str): The call number of the item.
        - num_of_copies (int): The number of copies available for the item.
        """
        title, call_number, num_of_copies = args

        self.title = title
        self.call_number = call_number
        self.num_of_copies = int(num_of_copies)

    def check_availability(self):
        """
        Checks if the item is available for checkout.

        Returns:
        - bool: True if the item is available, False otherwise.
        """
        return self.num_of_copies > 0

    @abc.abstractmethod
    def __str__(self):
        """
        Abstract method to return a string representation of the item.
        """
        pass
