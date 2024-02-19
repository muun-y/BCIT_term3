from enum import Enum


class BudgetCategory(Enum):
    """Enumeration for budget categories."""

    GAMES_AND_ENTERTAINMENT = "Games and Entertainment"
    CLOTHING_AND_ACCESSORIES = "Clothing and Accessories"
    EATING_OUT = "Eating Out"
    MISCELLANEOUS = "Miscellaneous"


class Budget:
    """A class representing a budget for a specific category.

    Attributes:
        categoryname (BudgetCategory): The category of the budget.
        amount (int): The amount allocated for the budget.
        transactions (list): A list of transactions related to this budget.
    """

    def __init__(self, categoryname, limit, amount):
        """
        Initializes a new Budget object with the specified details.

        :param categoryname (BudgetCategory): The category of the budget.
        :param amount The amount allocated for the budget.
        """
        self.categoryname = categoryname
        self.limit = limit
        self.amount = amount
        self.isLocked = False
        self.transactions = []
