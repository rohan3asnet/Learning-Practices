x,y,z=input('Enter three integer values:\n').split()
if x>y and x>z:
    print(x,'is greater')
elif y>x and y>z:
    print(y,'is greater')
else:
    print(z,"is greater")