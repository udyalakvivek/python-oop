"""
source code for the Student class
https://github.com/udyalakvivek/python-oop
"""

#snake case -- function_name, variable_name, module_name, package_name  ex: my_function, my_variable, my_module, my_package
#camel case -- class_name, method_name  ex: MyClass, myMethod
#method is a function that is defined inside a class. It is used to define the behavior of an object.
#function is a block of code that is defined outside a class. It is used to perform a specific task.

class Student:
    def __init__(self, name, age=18):
        self.name = name
        self.age = age
        self.course = []  # default value of course is an empty list  we can use as None but it is not a good practice to use None as default value for mutable data types like list, dict, set etc. because it can lead to unexpected behavior.

    def add_course(self, course_name):
        if (course_name in self.course):
            raise Exception("Course already exists")
        """Add a course to the student's course list."""
        self.course.append(course_name)

    #dunder method -- dunder == double underscore operator overloading -- operator overloading
    def __str__(self):  # this work just string representation of the objets
        return f"Student(name={self.name}, age={self.age}, course={self.course})"

    def __repr__(self):  # this work just string representation of the objets
        return str(self)



#fields , attributes
#behavior , methods

# student1 = [Student("Vivek", 25), Student("Rahul", 22)]

student1 = Student("Vivek", 23)
print(student1.name)
print(student1.age)

student2 = Student("Rahul")
print(student2.name)
print(student2.age)  # default value of age is 18

student3 = Student("Rohit", 20)
print(student3.name)
print(student3.age)
# access the course attribute
student3.course.append("MCA")  # but this is not a good practice use a method to add always use course to the course list

print(student3.course)


s4 = Student("Chunmung", 21)
print(s4.name)
s4.add_course("BCA")
s4.add_course("MCA")
print(s4.course)  # ['BCA', 'MCA']

