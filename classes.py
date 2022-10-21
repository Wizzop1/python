class Person:
    def __init__(self,name,age): #initialize
        self.name=name
        self.age=age
    def __str__(self): #way to print the class
        return f"{self.name}({self.age})"
    def present(self): #Object
        print('My name is ', self.name, 'I am ', self.age, 'years old.')
class Students(Person):
    pass
person1=Person("Deer", 20)
student1=Students("Mike", 15)
student1.present()
person1.name="John" #change value
person1.present()
