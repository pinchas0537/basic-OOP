class Point:
    def __init__(self, x ,y ):
        self.x = x
        self.y = y


class Line:
    counter = 0
    def __init__(self,a,b):
        self.a = a
        self.b = b
        Line.counter += 1
        
    def show(self):
        print(p1.x,p1.y)
        print(p2.x,p2.y)
    
    @classmethod
    def how_many(cls):
        print(cls.counter)

    @staticmethod
    def is_horizontal(line):
         return line.a.y == line.b.y
           
        
    @staticmethod
    def is_vertical (line):
        return line.a.x == line.b.x
            
               
if __name__ == "__main__":   
            
    p1 = Point(13,13)
    p2 = Point(12,13)
    l = Line(p1,p2)

    print(l.is_horizontal(l))
    print(l.is_vertical(l))
    l.how_many()
    l.show()