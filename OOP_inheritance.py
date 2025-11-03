# class Vehicle:
    
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
        
#     def move(self):
#         print("The vehicle is moving")
    
# class Car(Vehicle):
    
#     def move(self):
#         return "The car drives"
    
# class Plane(Vehicle):
    
#     def move(self):
#         return "The plane flies"
    
# v = Vehicle("FORD", "EXPLORER")
# v.move()

# c = Car("FORD", "EXPLORER")
# print(c.move())

# p = Plane("FORD", "EXPLORER")
# print(p.move())
    
class Animals:
    
    def __init__(self,name):
        self.name = name
    
    def sound(self):
        return " "
    
class Dog(Animals):
    
    def sound(self):
        return "Woof"

class Cat(Animals):
    
    def sound(self):
        return "Meow"
a = Animals("tiger")

d = Dog("dog")

c = Cat("cat")

l = [a,d,c]
for i in l:
    print(i.sound())