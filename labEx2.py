import math
class Circle:
    def __init__(self,r):
        self.r=r
    def area(self):
        
        area=math.pi*(self.r**2)
        print("Area: ", "{:.3f}".format(area))
    def perimeter(self):
        perimeter = 2*math.pi*self.r
        print("Perimeter: ", "{:.3f}".format(perimeter))
result = Circle(float(input()))
result.area()
result.perimeter()