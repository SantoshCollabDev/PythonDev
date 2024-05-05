# Inheritance Example

import random

class Vehicle:
    """ This
    """
    def __init__(self,name) -> None:
        self.__name = name

    def get_name(self):
        return self.__name
    
    def calculate_price(self):
        return random.randint(100000, 1000000)
        
        

class Car(Vehicle):
    """ This
    """
    def calculate_price(self):
        return random.randint(100000,1000000)
    
    def __str__(self) -> str:
        return f"name: {self.get_name()}"

class Tractor(Vehicle):
    """ This
    """
    def calculate_price(self):
        return random.randint(300000,500000)
    
c1 = Car('Hondcity')
print(c1)
print(c1.get_name())
print(c1.calculate_price())

t1 = Tractor('Mahindra')
print(t1)
print(t1.get_name())
print(t1.calculate_price())
