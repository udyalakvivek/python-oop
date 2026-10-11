    # ==========================================
# 03 - INSTANCE METHODS
# ==========================================


class Student:

    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    # 1. Instance method
    def introduce(self):
        print(f"My name is {self.name}")
        print(f"My age is {self.age}")
        print(f"My course is {self.course}")

    # 2. Method that reads object state
    def get_course(self):
        return self.course

    # 3. Method with parameter
    def change_course(self, new_course):
        self.course = new_course

    # 4. Method that changes object state
    def change_age(self, new_age):
        self.age = new_age


# ==========================================
# Creating objects
# ==========================================

student1 = Student("Vivek", 25, "BCA")
student2 = Student("Rahul", 22, "B.Tech")


# ==========================================
# Calling instance methods
# ==========================================

student1.introduce()
student2.introduce()


# ==========================================
# Reading object state using a method
# ==========================================

course = student1.get_course()

print(course)


# ==========================================
# Changing object state using a method
# ==========================================

student1.change_course("MCA")
student1.change_age(26)


# ==========================================
# Checking changed state
# ==========================================

student1.introduce()



# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# Instance Methods Without __init__()
# ==========================================


class Student:

    # Instance method
    def introduce(self):
        print(f"My name is {self.name}")
        print(f"My age is {self.age}")
        print(f"My course is {self.course}")


# ------------------------------------------
# Create an object
# ------------------------------------------

student1 = Student()
print(student1.name)  # AttributeError: 'Student' object has no attribute 'name'

# ------------------------------------------
# Add instance attributes manually
# ------------------------------------------

student1.name = "Vivek"
student1.age = 25
student1.course = "BCA"


# ------------------------------------------
# Call instance method
# ------------------------------------------

student1.introduce()