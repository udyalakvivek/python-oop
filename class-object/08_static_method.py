"""
A method that belongs to a class rather than an instance of a class.
A static method is useful for functionality related to a class that doesn't need access to its instance or class data.
"""

class Car:
    total_car = 0 #creat a class variable
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
        Car.total_car += 1

    def full_name(self):  # Instance method
        return f"Brand : {self.brand} and Model: is {self.model}"

    def fuel_type(self):
        return f"'{self.model}' is a petrol car!"
    #this is a static a method
    @staticmethod
    def general_des():
        return "Cars are means of transport!!"

class Electric_car(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size

    def fuel_type(self):
        return f"'{self.model}' is a charging car!"


res = Car("TATA","Safari")
print(res.general_des())
# we can not access instanse method direct to class
print(Car.general_des())

# print(Car.fuel_type())
