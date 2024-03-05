# 1. Write a Python program to find a list of integers
# with exactly two occurrences of nineteen and at least three occurrences of five. 
# Return True otherwise False.
# Input:
# [19, 19, 15, 5, 3, 5, 5, 2]
# Output:
# True
# Input:
# [19, 15, 15, 5, 3, 3, 5, 2]
# Output:
# False
# Input:
# [19, 19, 5, 5, 5, 5, 5]
# Output:
# True

#1. yol
# def controlList(list):
#     countOndokuz=0
#     countBes=0


#     for i in list:
#         if i==19:
#             countOndokuz+=1
#         elif i==5:
#             countBes+=1
    
#     if countBes>=3 and countOndokuz==2:
#         return print("True")
#     else:
#         return print("False")


# list1=[19, 19, 15, 5, 3, 5, 5, 2] #True
# list2=[19, 15, 15, 5, 3, 3, 5, 2] #False
# list3=[19, 19, 5, 5, 5, 5, 5] #True 

# controlList(list1)
# controlList(list2)
# controlList(list3)

#2.yol
# def controlList(list):
#     if list.count(19)==2 and list.count(5)>=3:
#         return print("True")
#     else:
#         return print("False")


# list1=[19, 19, 15, 5, 3, 5, 5, 2] #True
# list2=[19, 15, 15, 5, 3, 3, 5, 2] #False
# list3=[19, 19, 5, 5, 5, 5, 5] #True 

# controlList(list1)
# controlList(list2)
# controlList(list3)

#  Write a Python program that accepts a list of integers and 
# calculates the length and the fifth element. 
# Return true if the length of the list is 8 and the fifth element occurs thrice in the said list.
# Input:
# [19, 19, 15, 5, 5, 5, 1, 2]
# Output:
# True
# Input:
# [19, 15, 5, 7, 5, 5, 2]
# Output:
# False
# Input:
# [11, 12, 14, 13, 14, 13, 15, 14]
# Output:
# True
# Input:
# [19, 15, 11, 7, 5, 6, 2]
# Output:
# False

# def checkList(list):
#     a=list[4]
#     for i in list:
#         if len(list)==8 and list.count(a)==3:
#             return print("True")
#         else:
#             return print("False")

# list1=[19, 19, 15, 5, 5, 5, 1, 2] #true
# list2=[19, 15, 5, 7, 5, 5, 2] #false
# list3=[11, 12, 14, 13, 14, 13, 15, 14] #true
# list4=[19, 15, 11, 7, 5, 6, 2] #false
# checkList(list1)
# checkList(list2)
# checkList(list3)
# checkList(list4)

# 4. We are making n stone piles! The first pile has n stones. 
# If n is even, then all piles have an even number of stones. 
# If n is odd, all piles have an odd number of stones. 
# Each pile must more stones than the previous pile but as few as possible. 
# Write a Python program to find the number of stones in each pile.

# Input: 2
# Output:
# [2, 4]
# Input: 10
# Output:
# [10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
# Input: 3
# Output:
# [3, 5, 7]
# Input: 17
# Output:
# [17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]

# def method(n):
#     list=[]

#     if n%2==0:      
#       a=n
#       for i in range(n):               
#         list.append(a)
#         a+=2 
#     else:
#       a=n
#       for i in range(n):        
#         list.append(a)
#         a+=2
#     return print(list)



# n=int(input("Bir sayi giriniz: "))
# method(n)

# Write a Python program to find a list of integers containing 
#exactly four distinct values, such that no integer repeats twice 
#consecutively among the first twenty entries.
# Input:
# [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
# Output:
# True
# Input:
# [1, 2, 3, 3, 1, 2, 3, 3, 1, 2, 3, 3, 1, 2, 3, 3]
# Output:
# False
# Input:
# [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
# Output:
# False

# def checkList(nums):

#     result=True

#     for i in range(len(nums)-1):
#         if nums[i]==nums[i+1]:
#           result=False

#     if result==True and len(set(nums))==4:
#        return print("True")
#     else:
#        return print("False")
    
#     #2.yol
#     # return all([nums[i] != nums[i + 1] for i in range(len(nums) - 1)]) and len(set(nums)) == 4

# list1=[1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4] #true
# list2=[1, 2, 3, 3, 1, 2, 3, 3, 1, 2, 3, 3, 1, 2, 3, 3] #false
# list3=[1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3] #false
# checkList(list1)
# checkList(list2)
# checkList(list3)