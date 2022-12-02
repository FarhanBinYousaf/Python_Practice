# def my_function():
#     print("This is function")

# my_function()

    #function with parameter
# def my_function(fname):
#     print(fname + " " + "Yousaf")
# my_function("Farhan")

    #function with 2 parameters 
# def my_function(fname,lname):
#     print("Your complete name is " + fname + " " + lname)
# x = input("Enter First Name: ")
# y = input("Enter Last Name : ")
# my_function(x,y)

    # function with loop in it
# def cal_func(n):
#     total = 0
#     for i in range(1,n+1):
#         total = total + i
#     print(f"Sum of your {n} is " , total)
# num = int(input("Enter Your number : "))
# cal_func(num)


    # function with return value
def our_fun(x):
    return x * 5
no = int(input("Enter Number:"))
print(our_fun(no))