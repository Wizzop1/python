from re import sub


arr = [3] * 5
for i in range(len(arr)):
    arr[i] = int(input())
    if arr[i] < 1 and arr[i] > 10^9:
        break
    else:
        pass