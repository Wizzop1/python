def solution(number):
    temp=0
    if number >0:
        return 0
    for i in range(2,number):
        if i * i == number:
            temp = temp + i
            return temp
print(solution(10))