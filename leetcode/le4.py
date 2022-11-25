def sorToInt(numb):
    l1 = [int(x) for x in str(numb)]
    l1.sort(reverse=True)
    var =''
    for item in l1:
        var += str(item)
    return var
num = 1235892
print(sorToInt(num))