n = int(input())
for i in range(1,n+1):
    if i == 1:
        print('*')
    else: 
        print(" "*(n-i),"*"*i,"*"*i," "*(n-i))
