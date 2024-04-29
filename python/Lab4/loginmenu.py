from budget import BudgetCategory
from transaction import Transaction
from usertype import Angel, Troublemaker, Rebel

class LoginMenu:
    def __init__(self, fam):
        self.fam = fam

    def display_option(self, selected_user):
        """
        Displays the menu options for the logged-in user.

        :param selected_user (User): The logged-in user.

        Prints the logged-in user's name and user type, followed by the available options.
        After displaying the options, prompts the user to enter their choice.
        If the input is valid, the corresponding action is executed.
        If the input is invalid, displays an error message and prompts the user to enter a valid choice.
        """
        print(f"\nLogged in as {selected_user.name} ({selected_user.userType})")
        print("Select from one of the options below: ")
        print("1.  View Budgets")
        print("2.  Record a Transaction")
        print("3.  View Transactions by Budget")
        print("4.  View Bank Account Details")
        print("5.  Logout")
        user_input = input("Enter your choice: ")

        if user_input == "1":
            self.print_view_budget(selected_user)
        elif user_input == "2":
            self.record_transaction(selected_user)
        elif user_input == "3":
            self.print_view_transactions_by_budget(selected_user)
        elif user_input == "4":
            self.print_view_bank_account_details(selected_user)
        elif user_input == "5":
            self.print_logout()
        elif user_input == "6":
            self.user_info(selected_user)
        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")

    def print_view_budget(self, selected_user):
        """
        Print the user's balance and budget allocations.

        :param selected_user: User object representing the user whose budget information is to be printed.
        """
        print(f"\n{selected_user.userType} {selected_user.name}'s balance is ${selected_user.bankaccount.bankBalance}")
        totalBudget = 0
        for budget in selected_user.budgets:
            totalBudget += budget.amount
            lockMessage = ""
            if budget.isLocked == True:
                lockMessage = "- Locked"

            print(f"{budget.categoryname.value} budget: ${budget.amount} {lockMessage}")
        if(totalBudget < selected_user.bankaccount.bankBalance):
            print(f"Notice: The balance ${selected_user.bankaccount.bankBalance} is greater than the combined value of budgets ${totalBudget} ${lockMessage}")
        elif(totalBudget > selected_user.bankaccount.bankBalance):
            print(f"Notice: The balance ${selected_user.bankaccount.bankBalance} is less than the combined value of budgets ${totalBudget}")
        
        print("\nReturning to the menu.\n")
        self.display_option(selected_user)

    def record_transaction(self, selected_user):
        print("Record a transaction")
        print("Please enter the following details about the transaction")

        # Transaction Category
        while True:
            print("1. Transaction Category")
            print("Please select the category of the transaction")
            # Instead of prompting the user to enter the name of the budget category,
            #  provide them with a list of categories and ask them to select one.
            for i, category in enumerate(BudgetCategory, start=1):
                print(f"    {i}: {category.name}")
            category_input = input("    Enter your choice: ")

            if category_input.isdigit() and 1 <= int(category_input) <= len(
                BudgetCategory
            ):
                category_input_index = int(category_input) - 1
                selected_category = list(BudgetCategory)[category_input_index]
                break
            else:
                print("Invalid input. Please enter a valid number\n")

        # Transaction Amount
        while True:
            print("2. Transaction Amount")
            amount_input = input("Enter the transaction amount: ")

            # The dollar amount (positive, non-zero number).
            if (amount_input.isdigit() and amount_input != "0") or (
                amount_input[0] == "-" and amount_input[1:].isdigit()
            ):
                amount_input = int(amount_input)
                break
            else:
                print("Invalid input. Please enter a valid number\n")

        # Transaction Location
        print("3. Transaction Location")
        location_input = input("Enter the transaction location: ")

        # Create transaction and check validation
        transaction = Transaction(selected_category, amount_input, location_input)

        # transaction validation check
        validationcheck = transaction.check_validation(selected_user)

        matching_budget = None
        for budget in selected_user.budgets:
            if budget.categoryname == selected_category:
                matching_budget = budget
                break
        
        userType = selected_user.userType
        
        if matching_budget is not None:
            if (validationcheck == True):
                matching_budget.transactions.append(transaction)
                matching_budget.amount -= amount_input
                print("Transaction added successfully.")
                if userType == "Angel":
                    angel = Angel()
                    angel.notification(selected_user, selected_category, amount_input)
                elif userType == "Troublemaker":
                    troublemaker = Troublemaker()
                    troublemaker.notification(selected_user, selected_category, amount_input)
                else:
                    rebel = Rebel()
                    rebel.notification(selected_user, selected_category, amount_input)
                self.fam.lock_user(selected_user)
            else:
                print(f"The transaction is REJECTED: The current balance of ${selected_user.bankaccount.bankBalance}")
        else:
            print("Error: No matching budget found for the selected category.")

        print("\nReturning to the menu.\n")
        self.display_option(selected_user)

    def print_view_transactions_by_budget(self, selected_user):
        """
        Print the transactions for a specific budget category.

        :param selected_user: User object representing the user whose transactions are to be printed.
        """
        print("View Transactions by Budget")
        print("Please select the budget category to view transactions")
        for i, category in enumerate(BudgetCategory, start=1):
            print(f"{i}. {category.value}")

        while True:
            user_input = input("Enter your choice: ")
            if user_input.isdigit() and 1 <= int(user_input) <= len(BudgetCategory):
                category_input_index = int(user_input) - 1
                selected_category = list(BudgetCategory)[category_input_index]

                break
            else:
                print("Invalid input. Please enter a valid number\n")

        print(f"\nTransactions for {selected_category.value} budget")
        for budget in selected_user.budgets:
            if budget.categoryname == selected_category:
                for transaction in budget.transactions:
                    print(transaction)
                    print()

        print("\nReturning to the menu.\n")
        self.display_option(selected_user)

    def print_view_bank_account_details(self, selected_user):
        """
        Print the user's bank account details.

        :param selected_user: User object representing the user whose bank account details are to be printed.
        """
        print(f"\nBank Account Details for {selected_user.name}")
        print(f"Bank Name: {selected_user.bankaccount.bankName}")
        print(f"Account Number: {selected_user.bankaccount.bankAccountNo}")
        print(f"Balance: ${selected_user.bankaccount.bankBalance}")

        print("\nReturning to the menu.\n")
        self.display_option(selected_user)

    def print_logout(self):
        """
        Logs the user out of the system and returns to the main menu.

        Prints a message indicating that the user has been logged out and returns to the main menu of the FAM system.

        """
        print("You have been logged out. Returning to the main menu.\n")
        self.fam.display_main_menu()

    #  User information test
    # def user_info(self, selected_user):
    #     print(f"**User info**")
    #     print(f"name: {selected_user.name}")
    #     print(f"age: {selected_user.age}")
    #     print(f"userType: {selected_user.userType}")

    #     print("\n")
    #     print(f"**Bank info**")
    #     print(f"bank account: {selected_user.bankaccount}")
    #     print(f"bank name: {selected_user.bankaccount.bankName}")
    #     print(f"bank account no: {selected_user.bankaccount.bankAccountNo}")
    #     print(f"bank balance: {selected_user.bankaccount.bankBalance}")
    #     print("\n")
    #     print(f"**Budgets**")
    #     for budget in selected_user.budgets:
    #         print(f"budgets categoryname: {budget.categoryname.value}")
    #         print(f"budgets amount: {budget.amount}")
    #         print("\n")
    #         for transaction in budget.transactions:
    #             print(f"transaction category: {transaction.budgetCategory.value}")
    #             print(f"transaction date: {transaction.date}")
    #             print(f"transaction amount: {transaction.amount}")
    #             print(f"transaction location: {transaction.locationName}")

    #     print("\n")
    #     print(f"**Lock status**")
    #     print(f"isLocked: {selected_user.isLocked}")

    #     print("\nReturning to the menu.\n")
    #     self.display_option(selected_user)
