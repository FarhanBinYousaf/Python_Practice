
# Normal Function 
# def add(a,b):
#     return a+b
# print(add(3,2))

# Lambda Function

# add2 = lambda a,b:a+b   # Lambda is ananymous function 
# print(add2(2,3))

 # Lamba Expression Practice

# Write a function that takes string as input and tells if length is greater than 5 using lambda

# Using Normal Function 
# def lenthChecker(s):
#     if len(s) > 5:
#         return True
#     else :
#         return False
# print(lenthChecker("Farhan"))   

# Using Lambda Function 

my = lambda s : True if len(s) > 5 else False 
print(my("Far"))