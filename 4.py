
print("Fill in the array")
arr = [int(x) for x in input().split()]
print("Number N:")
N = int(input())
if N <= len(arr):
    lNumber = arr[N]*arr[N]
    print(lNumber)
else:
    lNumber=-1
    print(lNumber)