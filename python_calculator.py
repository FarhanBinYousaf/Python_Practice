
# This is Python Calculator | Only for two numbers

first_number  = int(input("Enter First Number: "))
second_number = int(input("Enter Second Number: "))
 # Below is the list of all the functions defined in our program
def adition(x,y):
    add = x + y
    return add
def subtract(x,y):
    sub = x - y
    return sub
def multiply(x,y):
    mult = x * y 
    return mult
def division(x,y):
    div = x / y
    return div

print("Enter ..... ")
print("1. For Addition. ")
print("2. For Substraction. ")
print("3. For Multiplication. ")
print("4. For Division. ")
sugestion = int(input("Enter Your Choice.... "))
if sugestion == 1:
    print(f"Sum of {first_number} and {second_number} is :  ",adition(first_number,second_number))
elif sugestion == 2:
    print(f"Subtraction of {first_number} and {second_number} is :  ",subtract(first_number,second_number))
elif sugestion == 3:
    print(f"Multiplication of {first_number} and {second_number} is : ",multiply(first_number,second_number))
elif sugestion == 4:
    print(f"Division of {first_number} and {second_number} is : ",division(first_number,second_number)) 
else:
    # print("Sorry! Unknown suggestion") 
    quit      


