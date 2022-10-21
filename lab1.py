
class Var: 
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __print__(self):
        return f"{self.a}{self.b}{self.a+self.b}{self.a*self.b}"
    def present(self):
        print('a= ', self.a, 'b= ', self.b, "sum= ", self.a+self.b, "mul= ", self.a*self.b)
result=Var(4,5)
result.present()

