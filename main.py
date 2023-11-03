from account import *
from bank import *


def get_string_input(prompt):
    while True:
        try:
            user_input = input(prompt)
            if not user_input:
                raise ValueError("Input cannot be empty.")
            return str(user_input)
        except ValueError as e:
            print(f"Invalid input. Please enter valid string")


def get_integer_input(prompt):
    while True:
        try:
            user_input = input(prompt)
            if not user_input:
                raise ValueError("Input cannot be empty.")
            return int(user_input)
        except ValueError as e:
            print(f"Invalid input. Please enter valid integer")


def get_float_input(prompt):
    while True:
        try:
            user_input = input(prompt)
            if not user_input:
                raise ValueError("Input cannot be empty.")
            return float(user_input)
        except ValueError as e:
            print(f"Invalid input: Please enter valid float number")


def main():
    bank = Bank()
    try:
        bank.load_accounts_from_file("accounts.json")
    except FileNotFoundError:
        # Handle the case where the accounts file does not exist
        print("Accounts file not found. Creating a new one.")

    while True:
        print("----------------------------------------------------------------")
        print("\t\t\tWelcome to Bank\t\t\t")
        print("----------------------------------------------------------------")
        print("1. Create Bank Account")
        print("2. Withdraw from Account")
        print("3. Deposit to Account")
        print("4. Exit")

        choice = get_integer_input("Enter your choice: ")

        if choice == 1:
            print("1. Current Account")
            print("2. Deposit Account")
            print("3. Restricted Account")
            print("4. Account with Overdraft Facility")

            account_choice = get_integer_input("Enter your choice: ")

            if account_choice == 1:
                name = get_string_input("Enter your full name: ")
                account_number = get_string_input("Enter account number: ")
                initial_balance = get_float_input("Enter initial balance: ")
                account = CurrentAccount(name, account_number, initial_balance, 0)
                bank.add_account(account)
                print("Current Account created!")

            elif choice == 2:
                name = get_string_input("Enter your full name: ")
                account_number = get_string_input("Enter account number: ")
                initial_balance = get_float_input("Enter initial balance: ")
                account = DepositAccount(name, account_number, initial_balance, 5)
                bank.add_account(account)
                print("Deposit Account created!")

            elif choice == 3:
                name = get_string_input("Enter your full name: ")
                account_number = get_string_input("Enter account number: ")
                initial_balance = get_float_input("Enter initial balance: ")
                account = RestrictedAccount(name, account_number, initial_balance, 3)
                bank.add_account(account)
                print("Restricted Account created!")

            elif choice == 4:
                name = get_string_input("Enter your full name: ")
                account_number = get_string_input("Enter account number: ")
                initial_balance = get_float_input("Enter initial balance: ")
                account = AccountWithOverdraft(name, account_number, initial_balance, 2)
                bank.add_account(account)
                print("Account With Overdraft Facility created!")

        elif choice == 2:
            account_number = get_string_input("Enter account number: ")
            amount = get_float_input("Enter withdrawal amount: ")
            account = bank.find_account(account_number)
            if account:
                print(account.withdraw(amount))
            else:
                print("Account not found.")

        elif choice == 3:
            account_number = get_string_input("Enter account number: ")
            amount = get_float_input("Enter deposit amount: ")
            account = bank.find_account(account_number)
            if account:
                account.deposit(amount)
                print(f"Deposit successful. New balance: {account.balance}")
            else:
                print("Account not found.")

        elif choice == 4:
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

        try:
            bank.save_accounts_to_file("accounts.json")
        except IOError:
            print("Error saving account data to file.")


if __name__ == "__main__":
    main()
