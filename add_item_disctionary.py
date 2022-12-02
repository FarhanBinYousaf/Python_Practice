
myDisct = {
    "name" : "Harry",
    "Class" : "BS",
    "platform" : "Youtube",
    "1" : "F"
}

# print("Before adding new item : " ,myDisct)

 # Now i'm going to add new item to existing dictionary

# myDisct["color"] = "Red"     # This is how items are added in dictionary
# print("After adding new item : " , myDisct)

# myDisct.update({"color": "Red"})   # This method is also used to add items to dictionaries
# print("After adding item : " , myDisct)
# print("The Keys are : ", myDisct.keys())
# print("The Values are : ", myDisct.values())


print("Your Dictionary is : ", myDisct)
# print("Do you want to add items in Dictionary? Yes or No")
cond = input("Do you want to add items in Dictionary? Yes or No")
if cond == "Yes":
    leng = int(input("Dictionary Length: "))
    i = 0
    while i < leng:
        dicIndex = input("Enter Dictionary Index : ")
        dicValue = input("Enter Dictionary Value")
        myDisct.update({dicIndex: dicValue})
        print("After adding item to dictionary:" , myDisct)
        i = i + 1
else :
    print("Terminated")
