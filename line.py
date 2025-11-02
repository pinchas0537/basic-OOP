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
        print(self.a, self.b)
        
    @classmethod
    def how_many(cls):
        print(cls.counter)

    @staticmethod
    def is_horizontal(line):
        if line.a.y == line.b.y:
            return True
        else:
            return False
        
    @staticmethod
    def is_vertical (line):
        if line.a.x == line.b.x:
            return True
        else:
            return False
               
if __name__ == "__main__":   
            
    p1 = Point(13,13)
    p2 = Point(12,13)
    l = Line(p1,p2)

    print(l.is_horizontal(l))
    print(l.is_vertical(l))
    print(l.how_many())