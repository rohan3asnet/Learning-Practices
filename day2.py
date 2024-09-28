######return statement
# def area(length,breadth):
#     return length*breadth   #returning value 
# Area=area(7,7)
# print("The area is:",Area)


#####If statements
# on=True
# off=False
# condition=input("enter the conditon")
# def power(condition):
#     if condition==on:
#         print("Welcome to your desktop$$$$$$$$$")
#     else:
#         print("power is not turned yet!!!!!!")
# power(condition)

#######CALCULATOR#########
# num1=float(input("Enter the first number: "))
# num2=float(input("Enter the second number: "))
# print("1. Addition\n 2. Subtraction\n 3. Multiply\n 4. Division\n ")
# operation=int(input("Choose any of the above number to perform operation: "))

# if operation==1:
#     print("Added value is: ",num1+num2)
# elif operation==2:
#     print("Subtracted value is: ",num1-num2)
# elif operation==3:
#      print("Multiplied value is: ",num1*num2)
# elif operation==4:
#      print("Divided value is: ",num1/num2)

#####Dictionaries
#dictonaries contain specific key of different value
# monthConversions={
#     "Jan": "January",
#     "Feb": "Feburary",
#     "Mar":"March",
#     "Apr":"April",
#     "May":"May",
#     "Jun":"June",
#     "Jul":"July",
#     "Aug":"August",
#     "Sep":"September",
#     "Oct":"October",
#     "Nov":"November",
#     "Dec":"December",
# }
# #accessing dictionaries
# print(monthConversions["Sep"])


###for loops
# HSRcharacter=["Welt", "Dan", "Himeko", "March"]
# for character in HSRcharacter:
#     print(character)

#####exponent function
#print(4**5)
# def raiseToThePower(baseNum, powerNum):
#     result=1
#     for index in range(powerNum):
#         result=result*baseNum
#     return result

# print(raiseToThePower(2,5))
    
####2d list
# matrix=[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# print(matrix[1][2]) #matrix[row index][column index]

# ####nested for looop
# for row in matrix:
#     for column in row:
#         print(column)

