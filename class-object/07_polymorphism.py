class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"Brand : {self.brand} and Model: is {self.model}"
    #main example for polymorphism see in both class have same name function but work defferently as per obj
    def fuel_type(self):
        return f"'{self.model}' is a petrol car!"

class Electric_car(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size

    def fuel_type(self):
        return f"'{self.model}' is a charging car!"


res = Car("TATA","Safari")
print(res.brand)
print(res.model)
print(res.fuel_type())



my_electric_car = Electric_car("TATA","Punch", "85KW")
print(my_electric_car.model)
print(my_electric_car.full_name())
print(my_electric_car.fuel_type())


# hanlde a counter of all cars in same example 

class Car:
    total_car = 0 #creat a class variable
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
        Car.total_car += 1

    def full_name(self):
        return f"Brand : {self.brand} and Model: is {self.model}"

    def fuel_type(self):
        return f"'{self.model}' is a petrol car!"

class Electric_car(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size

    def fuel_type(self):
        return f"'{self.model}' is a charging car!"


res = Car("TATA","Safari")
Car("Hello","hi")
my_electric_car = Electric_car("TATA","Punch", "85KW")
print(Car.total_car) #

