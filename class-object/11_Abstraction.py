"""
    Abstract Base Class (ABC) is used to achieve data abstraction by defining a common interface for its subclasses. 
    It cannot be instantiated directly and serves as a blueprint for other classes.
    Abstract classes are created using abc module and @abstractmethod decorator, 
    allowing developers to enforce method implementation in subclasses while hiding complex internal logic
"""
#Abstraction means hiding implementation details and showing only the essential features to the user
from abc import ABC, abstractmethod

#without Abstract
class Payment:
    def pay(self,amount):
        print(f"Processing payment of ₹{amount}")

class UpiPayment(Payment):
    pass

class CardPayment(Payment):
    pass

upi = UpiPayment()
upi.pay(500)

card = CardPayment()
card.pay(1000)
#esmein kisi ke pass apna pay nhi hai sb parent ka use kar rhe hai 




#with
class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class UpiPayment(Payment):
    def pay(self, amount):
        print(f"Paying ₹{amount} using UPI")

class CardPayment(Payment):
    def pay(self, amount):
        print(f"Paying ₹{amount} using Card")

upi = UpiPayment()
upi.pay(500)

card = CardPayment()
card.pay(1000)
#emsin sbka apna apna pay method hai koi bhi parent ka use nhi kar rha sbka apna apna logic hai  