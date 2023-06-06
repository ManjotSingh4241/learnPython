# print("Hello World")
# Escape sequence chanracter \n
# print("Hello World\nI am Manjot Singh")
#################################################
# Variable and types
# a= 123
# print(a)
# b=True
# print(b)
# c = "Manjot"
# print(c)
# d = None
# print(d)
##################################
#Arithmetic Operators

# print(5+6)
# print(5*6)
# print(5-6)
# print(5/6)
# print(5%6)
############################
#Typecasting

# a = "1"
# b = "2"
# print(a + b)#this will print 12 because a and b is string not int, we need to convert this into int

# print(int(a)+int(b))#this will print 3 as it converts string into int

###################################################################
#Input.

# a = input("Enter your name ")
# print("My name is", a)

# x = input("Enter your First Number: ")
# y = input("Enter your second Number: ")

# print("Your Number is: ",int(x)+int(y))


###############################################################
#Strings

# name = "Manjot"
# friend = "Manak"
# anotherFriend = "Abhi"
# apple = '''He said,
# Hi Harry
# hey I am good
# "I want to eat an apple'''

# print("Hello", name)
# print(apple)
# print(friend[0])
# print(friend[3])

# for i in name:
#     print(i)
####################################################3

#String Slicing

# names = "Manjot, Singh"
# print(names[0:6])#to print characters from 0 to 5
# print(len(names))
#######################################################
#Different String Methods

# a = "!!Manjot!!  !! Singh!!" #Strings are imutable
# print(len(a))
# print(a.upper())
# print(a.lower())
# print(a.rstrip("!")) #To remove something from back of string
# print(a.replace("Manjot", "Jot"))
# print(a.split(" "))
# Heading = "introduction"
# print(Heading.capitalize())#To capitalize first character and converts every otehr thing to lower

# str1 = "Welcome to python"
# print(len(str1))
# print(len(str1.center(50)))

# b = "Manjot !! Manjot"
# print(b.count("Manjot"))

###########################################
#If Elif Else

# a = int(input("Enter Your Age: "))
# print("Your age is: ",a)

# if (a>=18 and a<= 99):
#     print("You can drive!")
# elif(a>99):
#     print("Not Possible")
# elif(a<18):
#     print("Cannot drive")
# else:
#     print("Hi!")
