class Account:
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount

    def get_balance(self):
        return self.balance


class BankingSystem:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, account_holder):
        if account_number in self.accounts:
            raise ValueError("Account number already exists.")
        self.accounts[account_number] = Account(account_number, account_holder)
        print(f"Account created successfully for {account_holder} with account number {account_number}.")

    def deposit_money(self, account_number, amount):
        if account_number not in self.accounts:
            raise ValueError("Account number does not exist.")
        self.accounts[account_number].deposit(amount)
        print(f"Deposited {amount} to account {account_number}. New balance is {self.accounts[account_number].get_balance()}.")

    def withdraw_money(self, account_number, amount):
        if account_number not in self.accounts:
            raise ValueError("Account number does not exist.")
        self.accounts[account_number].withdraw(amount)
        print(f"Withdrew {amount} from account {account_number}. New balance is {self.accounts[account_number].get_balance()}.")

    def check_balance(self, account_number):
        if account_number not in self.accounts:
            raise ValueError("Account number does not exist.")
        balance = self.accounts[account_number].get_balance()
        print(f"Account {account_number} balance: {balance}")

    def menu(self):
        while True:
            print("\nBanking System Menu:")
            print("1. Create Account")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Check Balance")
            print("5. Exit")
            choice = input("Enter your choice: ")

            try:
                if choice == '1':
                    account_number = input("Enter account number: ")
                    account_holder = input("Enter account holder name: ")
                    self.create_account(account_number, account_holder)
                elif choice == '2':
                    account_number = input("Enter account number: ")
                    amount = float(input("Enter amount to deposit: "))
                    self.deposit_money(account_number, amount)
                elif choice == '3':
                    account_number = input("Enter account number: ")
                    amount = float(input("Enter amount to withdraw: "))
                    self.withdraw_money(account_number, amount)
                elif choice == '4':
                    account_number = input("Enter account number: ")
                    self.check_balance(account_number)
                elif choice == '5':
                    print("Exiting the system. Goodbye!")
                    break
                else:
                    print("Invalid choice. Please enter a number between 1 and 5.")
            except ValueError as e:
                print(f"Error: {e}")


if __name__ == "__main__":
    banking_system = BankingSystem()
    banking_system.menu()
