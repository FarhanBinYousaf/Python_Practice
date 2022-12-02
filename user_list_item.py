

        # Dyanmic Insertion of items in list

# yourlist = ["Pakistan","India","China","USA"]
# print("Your Current list is:  " , yourlist)

# item = input("Enter item to insert into list: ")
# index = int(input("On which index : "))
# yourlist.insert(index, item)
# print("Your Updated list " ,yourlist)




    # Insertion throught loop in list 
lent = int(input("Enter the length of list you want : "))
mylist = []
i = 0
while i < lent:
    item = input("Enter item to insert:")
    mylist.append(item)
    i = i + 1
print("Your created list is :" , mylist)  
print("Do You want to remove item from list?")
cond = int(input("Enter 1 to remove items or 0 to terminate program"))
if cond == 1:
    item2 = input("Enter item to remove from list : ")
    mylist.remove(item2)
    print("List after removel of item", mylist)
else:
    print("Terminated")
    # Dynamic Removel of items from list
