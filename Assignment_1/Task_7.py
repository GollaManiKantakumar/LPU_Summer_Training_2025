class BankAccount:
    def __init__(self, account_number, holder_name, balance=0.0):
        self.__account_number = account_number
        self.__holder_name = holder_name
        self.__balance = balance

    def get_account_number(self):
        return self.__account_number

    def get_holder_name(self):
        return self.__holder_name

    def get_balance(self):
        return self.__balance

    def set_account_number(self, account_number):
        self.__account_number = account_number

    def set_holder_name(self, holder_name):
        self.__holder_name = holder_name

    def set_balance(self, balance):
        if balance >= 0:
            self.__balance = balance
        else:
            print("Balance cannot be negative.")

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.__balance:
            print("Insufficient balance.")
        else:
            self.__balance -= amount
            print(f"₹{amount} withdrawn successfully.")

    def display_account_info(self):
        print("\n--- Account Information ---")
        print("Account Number:", self.__account_number)
        print("Account Holder:", self.__holder_name)
        print("Balance: ₹", self.__balance)


def main():
    print("Welcome to the Bank Account Management System")

    acc_number = input("Enter Account Number: ")
    holder_name = input("Enter Account Holder Name: ")

    while True:
        try:
            balance = float(input("Enter Initial Balance: ₹"))
            break
        except ValueError:
            print("Invalid input. Please enter a numeric balance.")

    account = BankAccount(acc_number, holder_name, balance)

    while True:
        print("\n=== Menu ===")
        print("1. Display Account Info")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Update Account Holder Name")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            account.display_account_info()

        elif choice == '2':
            try:
                amount = float(input("Enter amount to deposit: ₹"))
                account.deposit(amount)
            except ValueError:
                print("Invalid amount. Please enter a number.")

        elif choice == '3':
            try:
                amount = float(input("Enter amount to withdraw: ₹"))
                account.withdraw(amount)
            except ValueError:
                print("Invalid amount. Please enter a number.")

        elif choice == '4':
            new_name = input("Enter new account holder name: ")
            account.set_holder_name(new_name)
            print("Account holder name updated successfully.")

        elif choice == '5':
            print("Thank you for using the system. Goodbye!")
            break

        else:
            print("Invalid choice. Please select from 1 to 5.")

if __name__ == "__main__":
    main()
