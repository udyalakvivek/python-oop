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