class BankAccount:
    """A class representing a bank account.

    Attributes:
        bankName (str): The name of the bank.
        bankAccountNo (str): The account number of the bank account.
        bankBalance (int): The balance of the bank account.
    """

    def __init__(self, bankName, bankAccountNo, bankBalance):
        """
        Initializes a new BankAccount object with the specified details.

        :param bankName (str): The name of the bank.
        :param bankAccountNo (str): The account number of the bank account.
        :param bankBalance (int): The balance of the bank account.
        """
        self.bankName = bankName
        self.bankAccountNo = bankAccountNo
        self.bankBalance = bankBalance

    def get_bank_balance(self):
        return self.bankBalance

    def set_bank_balance(self, transactionAmount):
        self.bankBalance = self.bankBalance - transactionAmount
