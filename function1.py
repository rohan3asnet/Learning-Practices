def gradeCalc(percentage):
    if(percentage>80):
        print('Distinction')
    elif(percentage<=80 and percentage>70):
        print('First Division')
    elif(percentage<=70 and percentage>60):
        print('Second Division')
    elif(percentage<=60 and percentage>40):
        print('Third Division')
    else:
        print("Fail")

percentage=float(input("Enter you percentage\n"))
percentage=float(percentage)
gradeCalc(percentage)