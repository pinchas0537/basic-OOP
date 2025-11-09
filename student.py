class Student:
    def __init__(self, name):
        self.__name = name
        
    def get_name(self):
        print(self.__name)
    def set_name(self, nwe_name):
        nwe_name == self.__name
        return nwe_name
    
    
class Vehicle:
    def __init__(self,brand, model):
        self.brand = brand
        self.model = model
        
    def start(self):
        return f"{self.brand}{self.model} engine started!"
    
class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)
        self.doors = doors
        
    def start(self):
        return super().start() + f", doors: {self.doors}"