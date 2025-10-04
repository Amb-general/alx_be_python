class BankAccount:
    def __init__(self, balance=0):
        """Initialize account with optional balance (default 0)."""
        self.__balance = balance  # private attribute

    def deposit(self, amount):
        """Deposit amount into account."""
        if amount > 0:
            self.__balance += amount
            return True
        return False

    def withdraw(self, amount):
        """Withdraw amount if sufficient funds exist."""
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return True
        return False

    def display_balance(self):
        """Return current balance."""
        return self.__balance

