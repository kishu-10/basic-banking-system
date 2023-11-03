import json

from account import Account


class Bank:
    """
    Basic representation of a bank class 
    where different types of accounts are available

    Attributes:
        accounts (list)
    """
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        """
        Method to add accounts in the bank
        """
        self.accounts.append(account)

    def find_account(self, account_number):
        """
        Method to find the account in the bank matching the account_number
        """
        if account_number in [account.account_number for account in self.accounts]:
            return next(
                (
                    account
                    for account in self.accounts
                    if account.account_number == account_number
                ),
                None,
            )
        return None

    def withdraw_from_account(self, account_number, amount):
        """
        Method to withdraw amount from the bank account
        """
        for account in self.accounts:
            if account.account_number == account_number:
                """
                When calling 'account.withdraw(amount)', the 'withdraw' method is  dynamically
                chosen based on the specific type of 'account' being processed and it also handles
                various account types without duplicated code which is a key feature of polymorphism.
                """
                return account.withdraw(amount)
        return (
            f"Bank account with account number: {account_number} cannot not be found."
        )

    def deposit_to_account(self, account_number, amount):
        """
        Method to deposit amount in the bank account
        """
        for account in self.accounts:
            if account.account_number == account_number:
                account.deposit(amount)
                return f"The amount has been deposited successfully. The new balance is: ${account.balance}"
        return (
            f"Bank account with account number: {account_number} cannot not be found."
        )

    def save_accounts_to_file(self, filename):
        """
        Method to save changes and updates of bank accounts in json file 
        """
        accounts_data = [account.account_details() for account in self.accounts]
        with open(filename, "w") as file:
            json.dump(accounts_data, file, indent=4)

    def load_accounts_from_file(self, filename):
        """
        Method to load bank accounts from the json file 
        """
        self.accounts = []
        try:
            with open(filename, "r") as file:
                accounts_data = json.load(file)
                for data in accounts_data:
                    account = Account(
                        data["name"],
                        data["account_number"],
                        data["balance"],
                        data["account_type"],
                    )
                    self.accounts.append(account)
        except Exception:
            pass
