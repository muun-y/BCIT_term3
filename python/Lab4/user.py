from bankaccount import BankAccount
from budget import Budget


class User:
    """A class representing a user in the FAM system.

    This class stores information about a user, including their name, age, user type, bank account details,
    budget allocations, and lock status.

    Attributes:
        name (str): The name of the user.
        age (int): The age of the user.
        userType (str): The type of the user (e.g., Angel, Troublemaker, Rebel).
        bankaccount (BankAccount): The user's bank account information.
        budgets (list): A list of Budget objects representing the user's budget allocations.
        isLocked (bool): A boolean indicating whether the user's account is locked or not.
    """

    def __init__(
        self,
        name,
        age,
        userType,
        bankName,
        bankAccountNo,
        bankBalance,
        budgets,
        isLocked,
    ):
        """
        Initializes a User object with the provided information.

        :param name (str): The name of the user.
        :param age (int): The age of the user.
        :param userType (str): The type of the user (e.g., Angel, Troublemaker, Rebel).
        :param bankName (str): The name of the user's bank.
        :param bankAccountNo (str): The account number of the user's bank account.
        :param bankBalance (int): The balance of the user's bank account.
        :param budgets (list): A list of Budget objects representing the user's budget allocations.
        :param isLocked (bool): A boolean indicating whether the user's account is locked or not.
        """
        self.name = name
        self.age = age
        self.userType = userType
        self.bankaccount = BankAccount(bankName, bankAccountNo, bankBalance)
        self.budgets = budgets
        self.isLocked = isLocked

    def __str__(self):
        """
        Returns a string representation of the User object.
        """
        return f"User: {self.name}, Age: {self.age}, Type: {self.userType}, Bank: {self.bankaccount}, Budgets: {self.budgets}"
