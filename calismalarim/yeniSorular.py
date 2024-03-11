#w3source

# Write a Python program that takes two digits m (row) and n (column) as input and generates a two-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
# Note :
# i = 0,1.., m-1
# j = 0,1, n-1.

# Test Data : Rows = 3, Columns = 4
# Expected Result : [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6]]


# i=int(input("satir sayisi girin: "))
# j=int(input("sutun sayisi giriniz: "))

# list = [[0 for col in range(j)] for row in range(i)]

# for row in range(i):
#     for col in range(j):
#         list[row][col]=row*col
# print(list)

# List Comprehension
#1 yol
# fruits=["apple","banana","cherry","kiwi","mango"]
# newList=[]

# for x in fruits:
#     if "a" in x:
#         newList.append(x)

# print(newList)

# 2. yol
# newList=[x for x in fruits if "a" in x]
# print(newList)

# not apple
# newList=[x for x in fruits if x !="apple"]
# print(newList)

