
num = 200

def func_one():
    num=100#local value
    global c
    c="no"
    print(num)

func_one()
print(num)#global value
print(c)