#traslator
# def translate(phrase):
#     translation=""
#     for letter in phrase:
#         if letter in "AEIOUaeiou":
#             if letter.isupper():
#                 translation=
#             translation=translation +"g"
#         else:
#             translation=translation + letter
#     return translation

# print(translate(input("Enter a phrase")))

# try:
#     x,y=map(int,input("enter two values ").split())
#     print(x/y)
# except:
#     print("invalid input, donot enter 0 as second input")


#####ReadWrite FIle

# demofile=open("demo.txt", "r")#open(filename, mode)
# # print(demofile.readable())#checking whether the file is readable or not, i.e read mode
# # print(demofile.readline())#read a single line
# # print(demofile.readlines()[0])#read specific line

# for line in demofile.readlines():
#     print(line)

# demofile.close()#always close you file

# hsrChar=open("demo.txt",'a')
# #print(hsrChar.read())
# #hsrChar.write("Herta")#if i again run this file then it will again append Herta following the end of Herta 
# #to add another character in the file in new line
# hsrChar.write("\nPomPom")
# hsrChar.close()

#writing file is for overwriting existing file or creating new file 

# ###CLASS AND OBJECT
# class student:
#     def __init__(self,name,rollno,address):
#         self.name=name
#         self.rollno=rollno
#         self.address=address
# #objects
# student1=student("Rohan",53,"kathmandu")
# student2=student("Preeti",50,"kathmandu")
# print(student1.rollno)


###inheritence
class Grandfather:
    def hair(self):
        print("curly")
    def complexion(self):
        print("dark")
    def height(self):
        print("tall")

class Father(Grandfather):
    def eyes(self):
        print("gray")

grandfather=Grandfather()
grandfather.complexion()

father=Father()
father.height()
father.eyes()