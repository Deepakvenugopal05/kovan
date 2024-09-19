from math import pi
class Shape():
    def __init__(self,length,height):
        self.length = length
        self.height = height
    def get_area(self):
        return self.length * self.height
    
class Rectangle(Shape):
    def __init__(self, length, height):
        super().__init__(length, height)

class Square (Rectangle):
    def __init__(self, length, height):
        super().__init__(length, height)
    
    def get_area(self):
        try:
            assert self.length == 0
            if (self.length == self.height):
                return self.length **2
            else:
                return "It is not a square"
        except:
            print('0 must not be provide')
class Triangle(Rectangle):
    def __init__(self, length, height):
        super().__init__(length, height)
    def get_area(self):
        try:
            return super().get_area() // 2
        except ArithmeticError as e:
            print(e)
        finally :
            print('No value returned from Rectangle(get_area())')
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def get_area(self):
            try:
                assert self.radius == 0
                return f"{pi* self.radius**2:.2f}"
            except AssertionError as e:
                print('0 must not be given')
try:
    length = int(input("Enter the length: "))
    height = int(input("Enter the height: "))
    

except ValueError:
    print("Incorrect value entered")

r1 = Rectangle(length,height)
print(r1.get_area())
s1 = Square(12,12)
print(s1.get_area())
c1 = Circle(3)
print(c1.get_area())
t1 = Triangle(12,3)
print(t1.get_area())
