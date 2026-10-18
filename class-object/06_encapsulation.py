"""
Encapsulation in Python means combining data and methods inside a class and controlling access to that data. We can use double underscores (__) to make attributes private-style and provide access through methods such as getters and setters.
"""


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
class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.__model = model # __ use for make private

    def full_name(self):
        return f"Brand : {self.brand} and Model: is {self.__model}"

    def get_model(self):
        return self.__model + "!"

    # Setter
    def set_model(self, model):
        self.__model = model

class Electric_car(Car):
    def __init__(self,brand , model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size


res = Car("TATA","Safari")
print(res.brand)
print(res.get_model())


#setter example
car = Car("TATA", "Safari")
print(car.get_model())  # Safari
car.set_model("Punch")
print(car.get_model())  # Punch



my_electric_car = Electric_car("TATA","Punch", "85KW")
print(my_electric_car.get_model())
print(my_electric_car.full_name())
