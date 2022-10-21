


my_int = int(input())
my_list = [int(x) for x in str(my_int)]
sum1=my_list[0]
for i in range(1, len(my_list)):
    if i < len(my_list):
        sum2=sum1
        sum1 = sum2 +my_list[i]
    elif i == (len(my_list)-1):
            sum1=sum2+my_list[i]
    else:
        print('fuck off')
        
print(my_list)
print(sum1)
if sum1%2==0:
    print('Even')
else:
    print('Odd')