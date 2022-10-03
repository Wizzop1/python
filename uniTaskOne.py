n = int(input())
conversion = int(input())
count=0
arr = []
if conversion == 2:
    while n>=0:
        arr.insert(count,int(n%2))
        n=n/2
print(arr)
