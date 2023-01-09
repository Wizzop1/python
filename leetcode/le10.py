def square_digits(num):
    plc = 0
    str1 =""
    for digit in str(num):
        plc = int(digit)**2
        str1 += str(plc)
    print(str1)


num = 9119
print(square_digits(num))