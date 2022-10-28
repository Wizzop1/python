def math(a,m_op,b):
    a=int(a)
    b=int(b)
    match m_op:
        case '+':
            print(a+b)
        case '-':
            print(a-b)
        case '*':
            print(a*b)
        case '/':
            print(a/b)
        case '//':
            print(a//b)

math(input("First number: "),input("Operation: "),input("Second number: "))

