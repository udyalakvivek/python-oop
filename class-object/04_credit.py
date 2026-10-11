#attributes = data members, fields,
#behaviors = methods

class CreditCard:
    def __init__(self, name, number, limit = 8000, bank = "Python Bank"):
        self.name = name
        self.number = number
        self.bank = bank
        self.balance = 0
        self.limit = limit
    
    def charge(self, amount):
        #not int or not not float
        if not (isinstance(amount, int) or  isinstance(amount, float)) or (amount <= 0):
            print("Charge Denied")
        else:
            self.balance += amount
    
    def pay(self, amount):
        if not (isinstance(amount, int) or  isinstance(amount, float)) or (amount <= 0):
            print("Charge Denied")
        else:
            self.balance -= amount
    #This is a special/dunder method.
    def __str__(self):
        """Return a string representation of the credit card information."""
        info = "Name: " + self.name + "\n"
        info += "Number: " + "XXXX" + self.number[4:] + "\n"
        info += "Bank: " + self.bank + "\n"
        info += "Balance: " + str(self.balance)
        return info

    def __repr__(self):
        """Return a string representation of the credit card object for debugging purposes."""
        return str(self)

card = CreditCard("Kenny", "12345678")
print(card)
print(card.__dict__)
card.charge(10000)
print(card)
card.charge(200)
print(card)

card.pay(5000)
print(card)


#learn use case of __str__ and __repr__ methods.
class Student:
    def __init__(self, name):
        self.name = name
    

student = Student("Vivek")

print(student)  # <__main__.Student object at 0x7f8c8c8c8c8c>


class Student:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"Student Name: {self.name}"

student = Student("Vivek")
print(student)  # Student Name: Vivek


