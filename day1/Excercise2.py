#Greatings.... 
import time
Name = "Manjot Singh"

timeStamp = int(time.strftime('%H'))
# print (timeStamp)
if(timeStamp> 24 and timeStamp<=12):
    print("Good Morning", Name)
elif(timeStamp>12 and timeStamp<= 4):
    print("Good Afternoon", Name)
else:
    print("Good Evening", Name)
