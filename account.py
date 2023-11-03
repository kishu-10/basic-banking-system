class Account:
    """
    Basic representation of a bank account and can be subclassed
    to create specialized account types with custom behavior

    Attributes:
        name (str), account_number (str), balance (float)
    """

    def __init__(self, name, account_number, balance, account_type=None):
        self.name = name
        self.account_number = account_number
        self.balance = balance
        self.account_type = account_type

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return f"The amount has been withdrawn successfully. Remaining balance is: ${self.balance}"
        else:
            return "The account has insufficient balance."

    def deposit(self, amount):
        self.balance += amount

    def __str__(self):
        return f"Account Name: {self.name}, Account Number: {self.account_number}, Account Type: {self.account_type}, Balance: ${self.balance}"

    def account_details(self):
        return {
            "name": self.name,
            "account_number": self.account_number,
            "account_type": self.account_type,
            "balance": self.balance,
        }


class CurrentAccount(Account):
    """
    This class provides functionality for a current account.
    It allows withdrawals and tracks the number of cheques issued.

    Attributes:
        name (str), account_number (str), balance (float), no_of_cheque (int)
    """

    def __init__(
        self,
        name,
        account_number,
        balance,
        no_of_cheque,
        account_type="Current Account",
    ):
        super().__init__(name, account_number, balance, account_type)
        self.no_of_cheque = no_of_cheque

    def withdraw(self, amount):
        super().withdraw(amount)
        self.no_of_cheque += 1


class DepositAccount(Account):
    """
    This class provides functionality for a deposit account.
    It allows withdrawals and manages the balance with assigned interest rate.

    Attributes:
        name (str), account_number (str), balance (float), interest_rate (float)
    """

    def __init__(
        self,
        name,
        account_number,
        balance,
        interest_rate,
        account_type="Deposit Account",
    ):
        super().__init__(name, account_number, balance, account_type)
        self.interest_rate = interest_rate

    def withdraw(self, amount):
        super().withdraw(amount)

    def deposit(self, amount):
        super().deposit(amount)
        self.balance += amount * self.interest_rate


class RestrictedAccount(Account):
    """
    This class provides functionality for a restricted account.
    It allows withdrawals but the number of withdrawls are limited.

    Attributes:
        name (str), account_number (str), balance (float), withdraw_limit (int)
    """

    def __init__(
        self,
        name,
        account_number,
        balance,
        withdraw_limit,
        account_type="Restricted Account",
    ):
        super().__init__(name, account_number, balance, account_type)
        self.withdraw_limit = withdraw_limit

    def withdraw(self, amount):
        if 0 < amount <= self.withdraw_limit and self.balance >= amount:
            self.balance -= amount
            return f"The amount has been withdrawn successfully. Remaining balance is: ${self.balance}"
        elif amount > self.withdraw_limit:
            return "Withdrawal amount has exceeded the maximum limit."
        else:
            return "The account has insufficient balance."


class AccountWithOverdraft(Account):
    """
    This class provides functionality for an over draft account.
    It allows withdrawals but the number of withdrawls are limited.

    Attributes:
        name (str), account_number (str), balance (float), overdraft_limit (int)
    """

    def __init__(
        self,
        name,
        account_number,
        balance,
        overdraft_limit,
        account_type="Over Draft Account",
    ):
        super().__init__(name, account_number, balance, account_type)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        available_balance = self.balance + self.overdraft_limit
        if amount <= available_balance:
            self.balance -= amount
            return f"The amount has been withdrawn successfully. Remaining balance is: ${self.balance}"
        else:
            return "Withdrawal amount has exceeded the maximum limit."
