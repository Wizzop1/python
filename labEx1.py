class ExerciseOne:
    def __init__(self,a,b,h):
        self.a=a
        self.b=b
        self.h=h
    def calcArea(self):
        print("{:.2f}".format((((self.a+self.b)*self.h)/2)))
result = ExerciseOne(float(input("Input A:")),float(input("Input B:")),float(input("Input H:")))
result.calcArea()
