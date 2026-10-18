# ==========================================
# CLASS AND OBJECT
# ==========================================

# create a class
class Person:
    """Class ek user-defined type / blueprint hoti hai jisse objects create kiye ja sakte hain
    A class is a user-defined type that defines the structure and behavior that its instances can have.
    """
    pass


# create an object of the class
obj = Person()
obj2 = Person()

# check the type of the object
print(type(obj))  # <class '__main__.Person'>
print(type(obj2))  # <class '__main__.Person'>

#check object identity
print(obj is obj2)  # False

#creating another object of the class
obj3 = Person()

obj4 = obj3  # obj4 is now referencing the same object as obj3
print(obj3 is obj4)  # True


class Car:
    def __init__(self,brand, model):
        self.brand = brand
        self.model = model
    def full_name(self):
        return f"Brand : {self.brand} and Model: is {self.model}"
result = Car("Toyota","Corolla")
print(result.brand)
print(result.model)

my_new_car = Car("TATA","Safari")
print(my_new_car.model)
print(my_new_car.full_name())