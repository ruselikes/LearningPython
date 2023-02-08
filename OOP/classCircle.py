import math
class Circle:
    def __init__(self,xcor = 0,ycor = 0, r = 1):
        self.x = xcor
        self.y = ycor
        self.radius = r
    def __repr__(self):
        return f"Circle: x={self.x}, y = {self.y},radius = {self.radius}, {self}"

    def find_area(self):
        print("S = pi * r^2 :\tR = {0},coords({1},{2}). Area: {3}".format(self.radius, self.x, self.y, math.pi * (self.radius)**2))
    def find_perimetr(self):
        print(f"P = 2 * pi * r:\t {2*math.pi * self.radius}")

    def is_intersection(self, second_circle):
        a = math.fabs(self.x) +  math.fabs(second_circle.x)
        b = math.fabs(self.y) +  math.fabs(second_circle.y)
        interval = (a**2 + b**2)**(1/2)

        if self.radius + second_circle.radius >= interval:#внешнее пересечение
            return  f"Detect circle's intersection"
        elif abs(self.radius - second_circle.radius) >= interval:#внутренее пересечение
            return f"Detect circle's intersection"
        else:
            return "There is no intersection"
circle1 = Circle(-1,0,r = 4)
circle2 = Circle(3,3,2)
circle1.find_area()
circle1.find_perimetr()
print(circle1.is_intersection((circle2)))
print(circle1)