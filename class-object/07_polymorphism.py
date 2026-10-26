"""
Polymorphism means "many forms" and allows the same method, function or operator to behave differently depending on the object or data it works with. This flexibility helps create more reusable, maintainable and scalable code.

Real-Life Example:

In an online payment system, different payment methods such as Credit Card, UPI, Wallet and NetBanking all use the same processPayment() method.
The method name remains the same, but each payment type performs its own specific payment process.

"""

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
print(Car.total_car)


#type of Polymorphism
#1 Compile time Polymorphism means method overloading
class Calculator:
    def multiply(self ,a = 1,b = 1,*args):
        result = a*b
        for num in args:
            result = result * num
        return result

calc = Calculator()
print(calc.multiply())
print(calc.multiply(4))
print(calc.multiply(2, 3))
print(calc.multiply(2, 3, 4))

#2 Run time Polymorphism Mrthod overridding
class Animal:
    def sound(self):
        return "Some generic sound"
class Dog(Animal):
    def sound(self):
        return "Bark"
class Cat(Animal):
    def sound(self):
        return "Meow"

animals = [Dog(), Cat(), Animal()]
for animal in animals:
    print(animal.sound())


"""
    Polymorphism refers to the ability of the same method or operation to behave differently based on object or context. 
    It mainly includes compile-time and runtime polymorphism
In compile time :
    Compile-time polymorphism allows multiple methods with the same name but different parameters, with the appropriate method selected before execution. 
    While languages like Java and C++ support this through method overloading
    example in python :
    class Calculator:
    def multiply(self, a=1, b=1, *args):
        result = a * b
        for num in args:
            result *= num
        return result

    calc = Calculator()
    print(calc.multiply())            
    print(calc.multiply(4))  
    print(calc.multiply(2, 3))       
    print(calc.multiply(2, 3, 4))
In Run time:
    Runtime polymorphism means that the behavior of a method is decided while program is running, 
    based on the object calling it
    #example in python:
    class Animal:
        def sound(self):
            return "Some generic sound"

    class Dog(Animal):
        def sound(self):
            return "Bark"
    
    class Cat(Animal):
        def sound(self):
            return "Meow"
    
    animals = [Dog(), Cat(), Animal()]
    for animal in animals:
        print(animal.sound())
    #result
    Bark
    Meow
    Some generic sound

    Explanation: 
        Here, sound method behaves differently depending on whether object is a Dog, Cat or Animal and this decision happens at runtime. 
        This dynamic nature makes Python particularly powerful for runtime polymorphism.

    """
