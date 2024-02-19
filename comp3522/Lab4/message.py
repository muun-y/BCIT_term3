from enum import Enum


class Message(Enum):
    """Enumeration for messages.

    This enumeration defines various messages that can be used within the FAM system.

    Attributes:
        LOCKED_MESSAGE (str): Message indicating that the user is locked and cannot be logged in.
        POLITE_MESSAGE (str): Reminder message about significant budget usage in a category.
        RUTHLESS_MESSAGE (str): Warning message about exceeding the budget, potentially leading to account lockout.
        USER_LOCK_MESSAGE (str): Message informing the user that their account has been temporarily locked due to excessive budget overages.
    """

    LOCKED_MESSAGE = "Error: This user is locked and cannot be logged in. Returning to the main menu.\n"
    POLITE_EXCEED_MESSAGE= "Reminder: You have exceeded your budget for this category."
    CATEGORY_EXCEED_MESSAGE_1 = "You have exceeded "
    CATEGORY_EXCEED_MESSAGE_2 = "% of your budget."
    CATEGORY_LOCK_MESSAGE = "Warning: Budget category exceeded! This category is locked."
    RUTHLESS_EXCEED_MESSAGE = "Warning: Budget category exceeded! Continued spending may result in account lockout."
    USER_LOCK_MESSAGE = "Your account has been temporarily locked due to excessive budget overages. Please contact to your parent."
