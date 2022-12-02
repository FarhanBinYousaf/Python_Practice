        # Without String Formatting 
# number1 = int(input("Enter First Number: "))
# number2 = int(input("Enter Second Number: "))
# number3 = int(input("Enter Third Number: "))
# avg = (number1 + number2 + number3)/3
# print("Average is : " + str(avg))
        
        # With String Formatting 
no1, no2, no3 = input("Enter First , Second and Third Number").split()
print(f" First number {no1} \n Second Number {no2} \n Third Number {no3}")
avg = int(no1)+int(no2)+ int(no3)
avg2 = avg / 3
print("Average of all numbers is " + str(avg2))
