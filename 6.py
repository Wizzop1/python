from operator import contains


argumentOne = input()
argumentTwo = input()
endOfOne = (len(argumentOne)/2)-1
if argumentOne.index(argumentTwo,int(endOfOne)):
    print("True")
else:
    print("False")