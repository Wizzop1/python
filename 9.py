def get_sum(a,b):
    if a==b:
        return a
    elif a>b:
        return sum(range(a+1, b))
    elif b>a:
        return sum(range(b+1, a))
    else:
        return "No"

value1 = get_sum(a = input())
value2 = get_sum(b = input())
print(get_sum)