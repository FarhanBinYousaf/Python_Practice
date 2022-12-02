
# from winreg import EnableReflectionKey


myDisct = {
    "Name" : "Volto",
    "color" : "Red",
    "model" : "latest"
}
print(myDisct)
print("Enter : ")
print("1. To Remove item from dictionary ")
print("2. To Clear dictionary")
print("3. To delete whole dictionary")
suggest = int(input("Enter Your Choise: "))
if suggest == 1:
    # print("We are going to remove item")
    index = input("Enter Index Value to remove item from dictionary:")
    if myDisct.pop(index):
        print("Your value has been poped from Dictionary", myDisct)
elif suggest == 2:
    # print("We are going to clear the dictionary")
    myDisct.clear()
    print("Your dictionary has been cleared successfully", myDisct)
elif suggest == 3:
    # print("we are going to delete the whole dictionary")
    del myDisct
    print ("Has been deleted" , myDisct)
else :
    print ("Terminated")    
