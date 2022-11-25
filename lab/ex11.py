n = int(input("Enter amount of numbers: "))
numbers = [0] * n
for i in range(len(numbers)):
    numbers[i] = int(input())
    print(max(numbers))
