# RECURSION

# def factorial(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return n* factorial(n-1)

# print(factorial(5));
# print(factorial(4));

# def fibonacci(n):
#     if(n==0):
#         return 0
#     elif(n==1):
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)

# print(fibonacci(6))
# print(fibonacci(11))

########################################## Searching

###Linear Search

# list = [2, 4, 6, 8, 9]


# def search(list, n):
#     i = 0
#     while i < len(list):
#         if list[i] == n:
#             print("found")
#             break
#         i = i+1
#     else:
#         print("not found")

# search([2, 4, 6, 7, 8], 2)

###Binary Search

# list = [4, 6, 7, 8, 9, 1, 23, 45, 67, 89, 245, 6666, 89799787]

# def search(list, n):
#     l = 0
#     u = len(list)-1

#     while l<= u:
#         mid = (l+u) // 2

#         if list[mid] == n:
#             return print("found")
#         else:
#             if list[mid] < n:
#                 l = mid+1
#             else:
#                 u = mid-1
#     return print("not found")

# search(list, 345678)

##################################Sorting

###Bubble Sort

# list = [3, 5, 1, 43, 2, 45, 21, 53, 9]

# for i in range(0, len(list)):
#     for j in range(0, len(list)-1):
#         if list[j]>list[j+1]:
#             c= list[j]
#             list[j]=list[j+1]
#             list[j+1]=c
# print(list)

###Insertion Sort

# list = [3, 5, 1, 43, 2, 45, 21, 53, 9]

# for i in range(1, len(list)):
#     c = i
#     while c > 0 and list[c] < list[c - 1]:
#         a = list[c]
#         list[c] = list[c - 1]
#         list[c - 1] = a
#         c = c - 1

# print(list)

###Selection Sort

list = [3, 5, 1, 43, 2, 45, 21, 53, 9]

for i in range(0, len(list)-1):
    for j in range(i+1, len(list)):
        if list[i] > list[j]:
            c=list[i]
            list[i]=list[j]
            list[j]=c
print(list)
