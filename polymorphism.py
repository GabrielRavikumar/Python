from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self,side):
        self.side = side

    def area(self):
        return self.side ** 2

class Triangle(Shape):
    def __init__(self,base,height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height * 0.5

class Pizza(Circle):
    def __init__(self,radius,toppings):
        super().__init__(radius)
        self.toppings = toppings

shapes = [Circle(4),Square(5),Triangle(3,4),Pizza(15,'pepperoni')]
for shape in shapes:
    print(f'{shape.area()}cm')
