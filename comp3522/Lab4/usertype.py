from abc import ABC, abstractmethod
from enum import Enum
from message import Message


class UserType(ABC):
    """Abstract base class representing a user type in the FAM system.

    This class defines abstract methods for notification, percentage calculation, and budget check.

    Attributes:
        None
    """

    @abstractmethod
    def notification(self, user, category, amount):
        """Send notification to the user based on the transaction.

        user (User): The user for whom the notification is sent.
            category (str): The category of the transaction.
            amount (int): The amount of money involved in the transaction.

        Returns:
            None
        """
        pass

    @abstractmethod
    def calculate_percentage(self, user, category):
        """Calculate the percentage of the budget allocated for a specific category.

        :param user (User): The user for whom the percentage is calculated.
        :param category (str): The category for which the percentage is calculated.

        :returns : The percentage of the budget allocated for the category.
        """
        pass


class Angel(UserType):
    """Represents an Angel user type in the FAM system.

    This user type receives notifications based on their budget usage.
    If the user exceeds 90% of a budget in a category, they receive a notification.
    If they exceed the budget in a category, they receive a polite notification.
    """

    def notification(self, user, category, amount):
        """Send notification to the user based on the transaction.

        Args:
            user (User): The user for whom the notification is sent.
            category (str): The category of the transaction.
            amount (int): The amount of money involved in the transaction.
        """
        ratio = self.calculate_percentage(user, category, amount)
        print("ratio: ", ratio)
        for budget in user.budgets:
            if budget.categoryname == category:
                if ratio > 100:
                    print(Message.POLITE_EXCEED_MESSAGE.value)
                elif ratio >= 90:
                    print(
                        f"{Message.CATEGORY_EXCEED_MESSAGE_1.value}90{Message.CATEGORY_EXCEED_MESSAGE_2.value}"
                    )
                break

    def calculate_percentage(self, user, category, amount):
        """Calculate the percentage of the budget allocated for a specific category.

        Args:
            user (User): The user for whom the percentage is calculated.
            category (str): The category for which the percentage is calculated.

        Returns:
            int: The percentage of the budget allocated for the category.
        """
        for budget in user.budgets:
            if budget.categoryname == category:
                return (budget.limit - budget.amount) / budget.limit * 100
        return 0


class Troublemaker(UserType):
    """Represents a Troublemaker user type in the FAM system.

    This user type receives notifications based on their budget usage.
    If the user exceeds 75% of a budget in a category, they receive a notification.
    If they exceed the budget in a category, they receive a polite notification.
    If they exceed 120% of the budget in a category, they get locked out of conducting transactions in that category.
    """

    def notification(self, user, category, amount):
        """Send notification to the user based on the transaction.

        Args:
            user (User): The user for whom the notification is sent.
            category (str): The category of the transaction.
            amount (int): The amount of money involved in the transaction.
        """
        ratio = self.calculate_percentage(user, category, amount)
        for budget in user.budgets:
            if budget.categoryname == category:
                if ratio >= 120:
                    print(Message.CATEGORY_LOCK_MESSAGE.value)
                    budget.isLocked = True
                elif ratio > 100:
                    print(Message.POLITE_EXCEED_MESSAGE.value)
                elif ratio >= 75:
                    print(
                        f"{Message.CATEGORY_EXCEED_MESSAGE_1.value}75{Message.CATEGORY_EXCEED_MESSAGE_2.value}"
                    )
                break

    def calculate_percentage(self, user, category, amount):
        """Calculate the percentage of the budget allocated for a specific category.

        Args:
            user (User): The user for whom the percentage is calculated.
            category (str): The category for which the percentage is calculated.

        Returns:
            int: The percentage of the budget allocated for the category.
        """
        for budget in user.budgets:
            if budget.categoryname == category:
                return (budget.limit - budget.amount) / budget.limit * 100
        return 0


class Rebel(UserType):
    """Represents a Rebel user type in the FAM system.

    This user type receives notifications based on their budget usage.
    If the user exceeds 50% of a budget in a category, they receive a notification.
    If they exceed the budget in a category, they receive a ruthless notification and get locked out of conducting transactions in that category.
    If they exceed the budget in 2 or more categories, they get locked out of their account completely.
    """

    def notification(self, user, category, amount):
        """Send notification to the user based on the transaction.

        Args:
            user (User): The user for whom the notification is sent.
            category (str): The category of the transaction.
            amount (int): The amount of money involved in the transaction.
        """
        ratio = self.calculate_percentage(user, category, amount)
        for budget in user.budgets:
            if budget.categoryname == category:
                if ratio >= 100:
                    print(Message.RUTHLESS_EXCEED_MESSAGE.value)
                    print(Message.CATEGORY_LOCK_MESSAGE.value)
                    budget.isLocked = True
                elif ratio >= 50:
                    print(
                        f"{Message.CATEGORY_EXCEED_MESSAGE_1.value}50{Message.CATEGORY_EXCEED_MESSAGE_2.value}"
                    )
                break

    def calculate_percentage(self, user, category, amount):
        """Calculate the percentage of the budget allocated for a specific category.

        Args:
            user (User): The user for whom the percentage is calculated.
            category (str): The category for which the percentage is calculated.

        Returns:
            int: The percentage of the budget allocated for the category.
        """
        for budget in user.budgets:
            if budget.categoryname == category:
                return (budget.limit - budget.amount) / budget.limit * 100
        return 0
