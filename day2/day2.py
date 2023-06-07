#Functions...

# def calculateGmean(a, b):
#     mean = (a*b)/(a+b)
#     print(mean)

# def isGreater(a, b):
#     if a>b:
#         print("a is big")
#     else:
#         print("b is big")

# def isLesser(a, b):
#     pass

# a = 9
# b = 80

# calculateGmean(a, b)

# isGreater(a, b)

#Function Arguments

# def average(a=9, b=3):
#     print("The average is: ", (a+b)/2)

# average(4)#default b = 3
# average(b=4)#default a = 9


def average(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    print("Average is:", sum/len(numbers))

average(23456787654323456787654, 5435, 535, 3, 535,353,53, 5,2)