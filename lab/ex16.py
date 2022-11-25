def square(a):
    return print("Face of square = ", int(a)*int(a))
def pravougulnik(a,b):
    return print("Face of rectangle = ", int(a)*int(b))
def triangle(a,b):
    return print("Face of triangle = ", (int(a)*int(b))/2)
print("1 = Square, 2 = Rectangle, 3 = Triangle")
n = int(input())
match n:
    case 1:
        square(input("Size of A: "))
        square()
    case 2:
        pravougulnik(input("Size of A: "),input("Size of B: "))
        pravougulnik()
    case 3:
        triangle(input("Size of A: "),input("Size of B: "))
        