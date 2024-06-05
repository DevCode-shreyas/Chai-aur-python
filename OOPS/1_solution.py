# class Car:
#     total_car = 0

#     def __init__(self,brand,model):
#        self.__brand = brand
#        self.__model = model
#        Car.total_car += 1

#     def get_brand(self):
#         return self.__brand

#     def full_name(self):
#         return f"{self.__brand} {self.__model}"
    
#     def fuel_type(self):
#         return "Petrol or Diesel"
    
#     @staticmethod
#     def general_desc():
#         return "cars are good for transportation"
    
#     @property
#     def model(self):
#         return self.__model
    



class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric charge"


my_tesla = ElectricCar("Tesla","Model S","100")

print(isinstance(my_tesla,Car))



print(my_tesla.battery_size)
print(my_tesla.model)
print(my_tesla.full_name())
print(my_tesla.__brand)
print(my_tesla.fuel_type())

my_car = Car("Tata","Safari")
my_car.model = "City"
print(my_car.model) 

print(my_car.general_desc())
print(Car.general_desc())
print(safari.fuel_type())
print(Car.total_car)



my_car = Car("Toyota","Corolla")

print(my_car.brand)
print(my_car.model)
print(my_car.full_name())


my_new_car = Car("Honda","Civic")
print(my_new_car.model)



class Battery:
    def battery_info(self):
        return "this is battery"

class Engine:
    def engine_info(self):
        return "this is engine"


class ElectricCarTwo(Battery,Engine,Car):
    pass


my_new_tesla = ElectricCarTwo("Tesla","Model S")
print(my_new_tesla.battery_info()) 
print(my_new_tesla.engine_info())