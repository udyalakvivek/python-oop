# Parent Class
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_details(self):
        return f"Employee: {self.name}, Salary: ${self.salary}"

# Child Class (inherits from Employee)
class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        # super() initializes the name and salary attributes from the parent class
        super().__init__(name, salary)
        self.programming_language = programming_language  # Unique to Developer

    # Overriding the parent's method to provide specific details
    def get_details(self):
        return f"Developer: {self.name}, Language: {self.programming_language}, Salary: ${self.salary}"

# ---- Using the Classes ----

# Parent instance
emp = Employee("John", 60000)
print(emp.get_details())
# Output: Employee: John, Salary: $60000

# Child instance
dev = Developer("Alice", 95000, "Python")
print(dev.get_details())
# Output: Developer: Alice, Language: Python, Salary: $95000
