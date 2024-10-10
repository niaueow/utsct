class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    def check_balance(self):
        print(f"Your current balance is: ${self.balance:.2f}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"${amount:.2f} has been deposited to your account.")
        else:
            print("Deposit amount must be greater than zero.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        elif amount <= 0:
            print("Withdrawal amount must be greater than zero.")
        else:
            self.balance -= amount
            print(f"${amount:.2f} has been withdrawn from your account.")

    def exit(self):
        print("Thank you for using the ATM!")
        return False

def display_menu():
    print("\n--- ATM Menu ---")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

def main():
    atm = ATM(100)  # Initial balance is set to $100
    running = True

    while running:
        display_menu()
        choice = input("Please choose an option: ")

        if choice == '1':
            atm.check_balance()
        elif choice == '2':
            try:
                amount = float(input("Enter amount to deposit: "))
                atm.deposit(amount)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '3':
            try:
                amount = float(input("Enter amount to withdraw: "))
                atm.withdraw(amount)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '4':
            running = atm.exit()
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
