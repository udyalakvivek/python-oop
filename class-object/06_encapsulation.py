class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner            # Public attribute
        self.__balance = balance      # Private attribute (prefixed with __)

    # Getter method: Safely read private data
    def get_balance(self):
        return self.__balance

    # Setter method: Safely modify private data with validation logic
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__balance}")
        else:
            print("Invalid deposit amount!")

# ---- Using the Class ----

account = BankAccount("Alice", 1000)

# 1. Accessing Public Data
print(account.owner)  # Output: Alice

# 2. Attempting to access Private Data directly
# print(account.__balance)
# ^ This will throw an AttributeError: 'BankAccount' object has no attribute '__balance'

# 3. Accessing and modifying data via controlled public methods
print(account.get_balance())  # Output: 1000
account.deposit(500)          # Output: Deposited $500. New balance: $1500
account.deposit(-50)          # Output: Invalid deposit amount!



#===================================================================
#do not use now this is for when we start learning about inheritance

class BankAccount:
    def __init__(self, owner, balance, account_type):
        self.owner = owner                 # Public attribute
        self.__balance = balance           # Private attribute
        self._account_type = account_type  # Protected attribute (prefixed with a single _)

    # Getter method: Safely read private data
    def get_balance(self):
        return self.__balance

    # Setter method: Safely modify private data with validation logic
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__balance}")
        else:
            print("Invalid deposit amount!")

# Creating a subclass to demonstrate "Protected" behavior in inheritance
class SavingsAccount(BankAccount):
    def display_account_info(self):
        # Subclasses can freely access protected attributes
        print(f"Account Owner: {self.owner}")
        print(f"Account Type: {self._account_type}")

        # Subclasses CANNOT directly access private attributes
        # print(self.__balance) # This would raise an AttributeError

# ---- Using the Classes ----

# Initialize the subclass
savings_acc = SavingsAccount("Alice", 1000, "High-Yield Savings")

# 1. Accessing Public Data
print(savings_acc.owner)  # Output: Alice

# 2. Accessing Protected Data via a subclass method
savings_acc.display_account_info()
# Output:
# Account Owner: Alice
# Account Type: High-Yield Savings

# 3. Accessing Protected Data externally (Technically allowed, but discouraged)
print(savings_acc._account_type)  # Output: High-Yield Savings
