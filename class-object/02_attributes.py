"""Understand what data an object stores, what an instance attribute is, and why different objects can have different data."""

class Student:
    pass


student1 = Student()
student2 = Student()

"""we created two objects of student class but dont have any meaningfull information . A student have name, age , roll  like data"""

# ==========================================
#  ATTRIBUTES # An attribute is data associated with an object
# ==========================================


class Student:

    def __init__(self, name, age, course): 
        """The __init__ method is a special method in Python classes. It is called when an object is created from the class and allows the class to initialize the attributes of the object.
        esmein self.name mein name wo value store hoga jo object create karte waqt pass kiya gaya hoga. self.age mein age store hoga aur self.course mein course store hoga. and name , age, course ye teen alag alag instance attributes hain. Different objects can have different data because each object has its own set of instance attributes. For example, student1 and student2 can have different names, ages, and courses even though they are both instances of the Student class.
        self.name  =  name
        ↑           ↑
        │           │
        object       parameter
        attribute
        self represents the current object/instance.
        """
        self.name = name
        self.age = age
        self.course = course


# Creating objects

student1 = Student("Vivek", 25, "BCA")
student2 = Student("Rahul", 22, "B.Tech")


# Accessing instance attributes

print(student1.name)
print(student1.age)
print(student1.course)

#changing the value of instance attributes
student1.name = "Vivek Kumar"
student1.age = 26
student1.course = "MCA"

print(student2.name)
print(student2.age)
print(student2.course)

"""
    Accessing the internal dictionary of instance attributes
"""
print(student1.__dict__)  # {'name': 'Vivek', 'age': 25, 'course': 'BCA'}
print(student2.__dict__)  # {'name': 'Rahul', 'age': 22, 'course': 'B.Tech'}