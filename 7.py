def listToString(lString):
    str1= ""
    return (str1.join(lString))

clearString = input()
lString = list(clearString)
if len(clearString)>4:
    for i in range(len(lString)):
            i+=1
            if i>4:
                lString[i-1] = '#'
                
print(listToString(lString))