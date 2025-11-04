from abc import ABC ,abstractmethod
from math import pi

class Shape(ABC):
    def __init__(self,type):
        self.type = type
    @abstractmethod
    def area(self):
        pass
class Circle(Shape):
    def __init__(self, radius):
        super().__init__("circle")
        self.radius = radius
    def area(self):
        return pi*self.radius**2
    
class Square(Shape):
    def __init__(self, side):
        super().__init__("square")
        self.side = side
    def area(self):
        return self.side**2

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("rectangle")
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    
    
class Payment(ABC):
    def __init__(self):
        pass
    @abstractmethod
    def pay(self,amount):
        pass
class CreditCardPayment(Payment):
    def pay(amount):
        print(f"The payment type is: CreditCardPayment, The amount received is: {amount}")
    