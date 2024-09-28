#WAP to enter 4- digit number and find the sum of first and last digit of the number.
ival=int(input('Enter the four digit number\n'))
if ival>9999:
    print('invalid digit\n')
else:
    lastDigit=ival%10
    while ival>9:
        ival=ival//10  #gives the floor value
        firstDigit=int(ival)
    sum=firstDigit+lastDigit
    print('The sum is:',sum)