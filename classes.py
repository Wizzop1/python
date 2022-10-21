class Person:
    def __init__(self,fname,lname,age): #initialize
        self.fname=fname
        self.lname=lname       
        self.age=age
    def __str__(self): #way to print the class
        return f"{self.fname}{self.lname}({self.age})"
    def present(self): #Object
        print('My name is ', self.name, 'I am ', self.age, 'years old.')
class Students(Person): #Inheritance
    def __init__(self,fname,lname,age):
        self.fname=fname
        self.lname=lname
        self.age=age
#person1=Person("Deer", 20)
#student1=Students("Mike", 15)
student2= Students("Georgi","Todorov",20)
print(student2)
#student1.present()
#person1.name="John" #change value
#person1.present()
