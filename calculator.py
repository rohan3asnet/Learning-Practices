a,b=input("Enter two values to perform arithmetic operation:\n").split()
a=int(a)
b=int(b)
print("Choose the desire action:\n1.Add\n2.Subtract\n3.Multiply\n4.Divide")

choice=input()
match choice:
    case '1':
        print("Result:",a+b)
    
    case '2':
        print("Result:",a-b)
    
    case '3':
        print("Result:",a*b)
    
    case '4':
        print("Result:",float(a)/float(b))

    case _:
        print("option is not available")