class BanAccount:
    
    def __init__(self,account_number,balance):
        self.account_number = account_number
        self.balance = balance
        
    def deposit(self,amount):
        self.balance += amount
        return self.balance
 
    def withdraw(self,amount):
        if self.balance > amount:
            self.balance -= amount
        else:
            return "There is no balance from the withdrawal."
        return self.balance

    def get_balance(self):
        return f"The balance is:{self.withdraw(420)}"
    
bank = BanAccount(141201,2000)
print(bank.get_balance())


class Rectangle:
    def __init__(self ,width ,height):
        self.width = width
        self. height = height
        
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2*(self.width + self.height)
    
rec = Rectangle(6,7)

print(rec.area())
print(rec.perimeter())


class Student:
    def __init__(self ,name ,grades = []):
        self.name = name
        self.grades = grades
        
    def add_grade(self,grade):
        result = self.grades
        result.append(grade)
        return result
    
    def average(self):
        sum_of_grades = 0
        for i in self.grades:
            sum_of_grades += i
        return sum_of_grades / len(self.grades)

student1 = Student("pinchas",[100,88,65,30])

print(student1.add_grade(56))
print(student1.average())


class Book:
    def __init__(self,title, author, pages, is_read):
        self.title = title
        self.author = author
        self.pages = pages
        self.is_read = is_read
        
    def mark_as_read(self):
        self.is_read = True
        return self.is_read
    
    def info(self):
        print(f"titel:{self.title}")
        print(f"author:{self.author}")
        print(f"pages:{self.pages}")
        print(f"is_read:{self.is_read}")
        
book = Book("aba","Moshe",32,True)

print(book.mark_as_read())
print(book.info())


class Counter:
    
    def __init__(self ,count = 0):
        self.count = count
    
    def increase(self):
        self.count += 1
    
    def decrease(self):
        self.count -= 1
    
    def reset(self):
        self.count = 0
    
    def get_value(self):
        return self.count
    
c1 = Counter()
c1.increase()
c1.reset()
c1.decrease()

print(c1.get_value())


class ShoppingItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def total_price(self):
        return self.price * self.quantity
    
shopping = ShoppingItem("p",50,4)
print(shopping.total_price())


class Timer:
    
    def __init__(self, seconds):
        self.seconds = seconds
    
    def set_time(self, sec):
        self.seconds = sec
        return self.seconds
    
    def get_time(self):
        mm = self.seconds // 60
        ss = self.seconds % 60
        print( f"{mm}:{ss}")
    
t = Timer(200)
t.get_time()
print(t.set_time(250))