"""
Module representing the Family Asset Management (FAM) system.

This module contains the FAM class, which manages user registration, login, and budget allocation.

"""

from budget import BudgetCategory, Budget
from user import User
from loginmenu import LoginMenu
from message import Message


class FAM:
    def __init__(self):
        """Class representing the Family Asset Management (FAM) system.

        Attributes:
            users (list): A list of registered users in the FAM system.
            loginMenu (LoginMenu): An instance of LoginMenu for user login functionality.
        """
        self.users = []
        self.loginMenu = LoginMenu(self)

    def display_main_menu(self):
        """
        Displays the main menu of the FAM system.
        """
        print("Welcome to the FAM! Select from the options below")
        print("1.  Register new user")
        print("2.  Login existing user")
        print("3.  Exit program")
        while True:
            user_input = input("Enter your choice: ")
            if user_input == "1":
                self.register_user()
                break
            elif user_input == "2":
                self.login_user()
                break
            elif user_input == "3":
                print("Exiting program...")
                exit()
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")

    def register_user(self):
        """
        Registers a new user to the FAM system.
        If the user selects option 1,
        open a new menu to allow the user to enter information about a new user
        (name, age, user type, balance, bank name, bank number, game budget, food budget, etc)
        """
        print("Registering a new user")
        name = input("Enter the user's name: ")
        age = input("Enter the user's age: ")

        userType = self.get_user_type_input()

        bankName = input("Enter the user's bank name: ")
        bankAccountNo = input("Enter the user's bank account number: ")
        bankBalance = int(input("Enter the user's bank balance: "))
        isLocked = False

        while True:
            print("Please enter the budget for the following items")
            budgets = []

            # Get budget input for each category
            for category in BudgetCategory:
                budget_amount = self.get_budget_input(category)
                budget = Budget(category, budget_amount, budget_amount)
                budgets.append(budget)

            # Print test the list of budgets
            # budgets_list = [(budget.categoryname, budget.amount)
            #                 for budget in budgets]
            # print(budgets_list)

            total_budget = sum(budget.amount for budget in budgets)

            # Check if the total budget exceeds the bank balance
            if total_budget <= bankBalance:
                user = User(
                    name,
                    age,
                    userType,
                    bankName,
                    bankAccountNo,
                    bankBalance,
                    budgets,
                    isLocked,
                )

                self.users.append(user)
                print(f"User '{name}' registered successfully.\n")
                break
            else:
                print(
                    "\nError: The total budget exceeds the bank balance. Please re-enter the budgets.\n"
                )

        # Return to the main menu after registering a new user
        self.display_main_menu()

    def get_budget_input(self, categoryname):
        """
        Gets budget input from the user for a specific category.

        :param categoryname (BudgetCategory): The category for which the user is entering the budget.

        Returns:
            int: The budget amount entered by the user.

        :raises ValueError: If the input is not a valid positive number.
        """
        while True:
            try:
                budget = int(
                    input(f"Enter budget for {categoryname.value}: "))
                if budget < 0:
                    raise ValueError("Budget must be a positive number.")
                return budget
            except ValueError as e:
                print(f"Error: {e}")
                print("Please enter a valid budget.")

    def get_user_type_input(self):
        """
        Get user input for the user type.
        Returns the selected user type as an instance of the appropriate class.
        """
        while True:
            # Display user type options
            print("Select user type:")
            print(" 1. Angel")
            print(" 2. Troublemaker")
            print(" 3. Rebel")

            userType_input = input("Enter type number: ")

            # Check if user input is valid
            if userType_input in ["1", "2", "3"]:
                # Convert user type input to appropriate class and return
                if userType_input == "1":
                    return "Angel"
                elif userType_input == "2":
                    return "TroubleMaker"
                elif userType_input == "3":
                    return "Rebel"
            else:
                print("Invalid input. Please enter a valid user type (1, 2, or 3).\n")

    def login_user(self):
        """
        Logs in an existing user to the FAM system.
        If the user selects option 2,
        open a new menu to allow the user to enter number of the user to login
        """
        print("\nLog in as: ")
        # Display the user's name, user type, and locked status
        for i in range(len(self.users)):
            locked_status = " - Locked" if self.users[i].isLocked else ""
            print(
                f"{i+1}. {self.users[i].name} ({self.users[i].userType}) {locked_status}"
            )
        user_input = input("Enter user number: ")

        selected_user = self.users[int(user_input) - 1]

        # Check if the selected user is locked
        if selected_user.isLocked:
            print(Message.LOCKED_MESSAGE.value)
            self.display_main_menu()  # Return to the main menu
        else:
            self.loginMenu.display_option(selected_user)

    def lock_user(self, selected_user):
        """
        Locks the selected user.
        """
        budgetLockCount = 0
        for budget in selected_user.budgets:
            if budget.isLocked:
                budgetLockCount += 1
        if budgetLockCount == 2:
            selected_user.isLocked = True
            print(f"User '{selected_user.name}' is now locked.\n")
            self.loginMenu.print_logout()

    def load_test_users(self):
        """
        Loads test users to the FAM system.
        """
        user1 = User("Garfield", 8, "Troublemaker", "CIBC", "CIBC123", 400, [
            Budget(BudgetCategory.GAMES_AND_ENTERTAINMENT, 100, 100),
            Budget(BudgetCategory.CLOTHING_AND_ACCESSORIES, 100, 100),
            Budget(BudgetCategory.EATING_OUT, 100, 100),
            Budget(BudgetCategory.MISCELLANEOUS, 100, 100)
        ], False)

        user2 = User("Snoopy", 11, "Rebel", "TD", "TD123", 1000, [
            Budget(BudgetCategory.GAMES_AND_ENTERTAINMENT, 100, 100),
            Budget(BudgetCategory.CLOTHING_AND_ACCESSORIES, 200, 200),
            Budget(BudgetCategory.EATING_OUT, 300, 300),
            Budget(BudgetCategory.MISCELLANEOUS, 400, 400)
        ], True)

        user3 = User("Mickey", 9, "Angel", "RBC", "RBC123", 500, [
            Budget(BudgetCategory.GAMES_AND_ENTERTAINMENT, 100, 100),
            Budget(BudgetCategory.CLOTHING_AND_ACCESSORIES, 100, 100),
            Budget(BudgetCategory.EATING_OUT, 100, 100),
            Budget(BudgetCategory.MISCELLANEOUS, 100, 100)
        ], False)
        self.users.append(user1)
        self.users.append(user2)
        self.users.append(user3)
        print("Test users loaded successfully.\n")
