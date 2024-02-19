from datetime import datetime


class Transaction:
    """A class representing a transaction.

    This class stores information about a transaction, including its category, amount, and location.

    Attributes:
        date (datetime): The timestamp representing the date and time when the transaction was recorded.
        budgetCategory (str): The category of the transaction.
        amount (int): The amount of money involved in the transaction.
        locationName (str): The name of the location where the transaction occurred.
    """

    def __init__(self, budgetCategory, amount, locationName):
        """
        Initializes a Transaction object with the provided information.

        :param budgetCategory (str): The category of the transaction.
        :param amount (int): The amount of money involved in the transaction.
        :param locationName (str): The name of the location where the transaction occurred.
        """
        self.date = datetime.now()
        self.budgetCategory = budgetCategory
        self.amount = amount
        self.locationName = locationName

    def __str__(self):
        """
        Returns a string representation of the Transaction object.
        """
        return f"Date: {self.date}\nCategory: {self.budgetCategory}\nAmount: ${self.amount}\nShop: {self.locationName}"

    def check_validation(self, selected_user):
        """
        Checks if the transaction is valid.

        :returen bool: True if the transaction is valid, False otherwise.
        """
        bankBalance = selected_user.bankaccount.bankBalance
        if bankBalance-self.amount < 0:
            return False
        else:
            selected_user.bankaccount.set_bank_balance(self.amount)
            return True
