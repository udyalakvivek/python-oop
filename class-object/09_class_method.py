class Car:
    total_car = 0
    def __init__(self,brand):
        self.brand = brand
        Car.total_car += 1


res = Car("TATA")
res2 = Car("BMW")

print(Car.total_car)  # 2 Car.total_car accesses the class variable directly. You don't need a class method just to read it.




class Car:
    total_car = 0
    def __init__(self, brand):
        self.brand = brand
        Car.total_car += 1

    @classmethod
    def reset_count(cls):
        cls.total_car = 0

Car("TATA")
Car("BMW")
print(Car.total_car)  # 2
Car.reset_count()
print(Car.total_car)  # 0


#property decorator use case ....
class Car2:
    def __init__(self, brand,model):
        self.brand = brand
        self.__model = model
    @property  # now you can not change model value
    def model(self):
        return self.__model



res = Car2("TATA","PUNCH")
print(res.model)
print(res.brand)
res.model = "Safari"
print(res.model)
print(res.model)
