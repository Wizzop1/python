import math
def is_square(n):    
    if math.sqrt(n) %1 == 0:
        return True
    return False
print(is_square(9))