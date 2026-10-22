""""
Constructors are special methods used to initialize objects when they are created from a class. Object creation and initialization are handled through the __new__() and __init__() methods. Constructors help assign initial values to object attributes and prepare objects for use.
"""
# The __new__() method creates and returns a new instance of the class.
# The __init__() method initializes the newly created object


class A:
    def __new__(cls):
        print("Creating instance")
        return super().__new__(cls)
    def __init__(self):
        print("Initializing instance")

A()


class A:
    def __new__(cls):
        print("Creating instance")
        #Since it does not explicitly return an object, it returns None.
        #Because no instance is created, __init__() is never called.
    def __init__(self):
        print("Initializing instance")

print(A()) #Creating instance #None


class Animal:
    def __str__(self):
        return "Animal Object"

class Person:
    def __new__(cls):
        return Animal()

    def __init__(self):
        print("Inside __init__")

print(Person()) #Animal Object
"""
Person.__new__() returns an instance of Animal.
Since the returned object is not an instance of Person, Person.__init__() is never executed.
print(Person()) calls Animal.__str__().
"""

class A:
    def __new__(cls, name):
        if not name:
            return None

        return super().__new__(cls)

    def __init__(self, name):
        self.name = name


obj1 = A("Vivek")
print(obj1.name)

obj2 = A("")
print(obj2)
