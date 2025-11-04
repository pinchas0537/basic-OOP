from abc import ABC , abstractmethod

class Vehicles:
    def __init__(self, max_speed):
        self.max_speed = max_speed
    def drive(self):
        print(f" The maximum speed is:{self.max_speed}")
        
class Car(Vehicles):
    pass
        
class Motorcycle(Vehicles):
    pass

c = Car(220)
m = Motorcycle(300)
c.drive()
m.drive()


class  Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
class Manager( Employee):
    def manage(self):
        print(f"My name is: {self.name} I'm manager, and my salary is: ${self.salary}")

class Developer( Employee):
    def write_code(self):
        print(f"My name is: {self.name}i'm developer full stack, and my salary is: ${self.salary}")
        
m = Manager("Evyatar",50000)
d = Developer("pinchas",35000)
m.manage()
d.write_code()

# class Shape(ABC):
#     @