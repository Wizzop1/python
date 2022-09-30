print("First number: ")
num1=input()
print("Arithmetical operator: ")
operator=input()
print("Second number: ")
num2=input()
if operator == '/':
    print(int(num1) / int(num2))
elif operator == '*':
    print(int(num1) * int(num2))
elif operator == '+':
    print(int(num1) + int(num2))
elif operator == '-':
    print(int(num1) - int(num2))
else:
    print('You did not input a right operator')