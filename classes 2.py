## Classes 2 from Python Crash Course

class Car:
    # simple attempt to describe a car
    def __init__(self, make, model, year):
        self.make= make
        self.model= model
        self.year = year
    
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
my_new_car = Car('tesla', 'model S', 2021)

name = my_new_car.get_descriptive_name()
print(name)

    
    