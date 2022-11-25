def turnToDict(n):
    l1 = list()
    for i in range(1,n+1):
        l1.append(i)
    l1_dict = dict.fromkeys(l1,l1[-1])
    for i in range(1,len(l1)+1):
        l1_dict[i] = l1[len(l1)-i]
    return l1_dict
print(turnToDict(6))