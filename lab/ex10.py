n = int(input('enter number'))
sum =0
while True:
    sum +=n%10
    n = n//10
    if not n:
        break
print (sum)