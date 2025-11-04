class Book:
    def __init__(self, title: str, author: str, content: str):
        self.title = title
        self.author = author
        self.content = content
    def __str__(self):
        return f"title: {self.title}, author: {self.author}, content: {self.content}"
         
class Save_book:
    def __init__(self):
        self.book_list = []
        
    def saved_to_list(self,book:Book):
        self.book_list.append(book)
        return self.book_list
    def print_list(self):
        for book in self.book_list:
            print(book)
    
book2 = Book("abc","xyz","momo")
saved_to_list = Save_book()
saved_to_list.saved_to_list(book2)
saved_to_list.print_list()



class Student:
    def __init__(self,name: str, grades: list[int]):
        self.name = name
        self.grades = grades

class GradeCalculator:
    def __init__(self):
        pass
    @staticmethod
    def average_grade(grades: Student):
        return sum(grades) / len(grades)
    
s = Student("momo",[100,89,76])
c = GradeCalculator()
print(c.average_grade(s.grades))



class Order:
    def __init__(self, items: list[str], total_price: float):
        self.items = items
        self.total_price = total_price

class InvoicePrinter:
    def __init__(self):
        pass
    @staticmethod
    def print_invoice(invoice: Order):
        print(f"The items are: {invoice.items}, The price is: {invoice.total_price} .")
        
orders = Order(['e','t'],78.34)
invoice_printer = InvoicePrinter()
invoice_printer.print_invoice(orders)