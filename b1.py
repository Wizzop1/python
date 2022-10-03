n = input()
count = 0
arr = []
psum = []
psum = ["b"] * int(n)
arr = ["b"] * int(n)
for i in range(int(n)):
    arr[i] = int(input().strip())
    if arr[i] < -10^9 and arr[i]>10^9:
        break
arr.sort(reverse=True)
print(arr)
for i in range(int(n)):
    if i == 0:
        psum[i] = arr[i]
    elif i>0:
        psum[i] = psum[i] + int(arr[i+1])
        if i== int(n)-1:
            psum[i] = psum[i] + arr[i]
    else:
        break
for i in range(len(psum)):    
    if psum[i] > 0:
        count = count + 1
print(count)