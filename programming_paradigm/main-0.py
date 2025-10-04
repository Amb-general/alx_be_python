import sys
from bank_account import BankAccount

def main():
    # Create account with optional starting balance (say 100)
    account = BankAccount(100)

    if len(sys.argv) < 2:
        print("Usage: python main.py <command> [amount]")
        return

    command = sys.argv[1].lower()

    if command == "deposit":
        if len(sys.argv) == 3:
            amount = float(sys.argv[2])
            if account.deposit(amount):
                print(f"Deposited: {amount}")
            else:
                print("Invalid deposit amount.")
        else:
            print("Usage: python main.py deposit <amount>")

    elif command == "withdraw":
        if len(sys.argv) == 3:
            amount = float(sys.argv[2])
            if account.withdraw(amount):
                print(f"Withdrew: {amount}")
            else:
                print("Insufficient funds.")
        else:
            print("Usage: python main.py withdraw <amount>")

    elif command == "display":
        print(f"Current Balance: {account.display_balance()}")

    else:
        print("Unknown command. Use deposit, withdraw, or display.")

if __name__ == "__main__":
    main()

