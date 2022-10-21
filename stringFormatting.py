

class Formatting:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def result(self):
        print('a = {} b = {} a+b = {}'.format(self.a,self.b,self.a+self.b))
        print(f'a = {self.a} b = {self.b} area = {self.a*self.b}')

printe = Formatting(4,6)
printe.result()