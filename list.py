# List ========> List are used to store multiple items in a single variable
# List ========> List can be ordered, changeable and allow duplicate 

# mylist = ["Pakistan","India","China","America","Turkey"]
# # print(type(mylist))
# print(mylist)
# print(len(mylist))

#     # Accessing the list items 
# print(mylist[1:4])   # the items at 4th index is not included 
# print(mylist[-1])    # (-1) means last item in list



    #insert items in list 
# addlist = ["Pakistan","India","China"]
# addlist.insert(2,"USA") 
# print(addlist)
    # Append items at the end of list
# apendlist = ["Pakistan","India","China"]
# apendlist.append("USA")
# print(apendlist)

    # Extend() methos use to 
firstList = ["Pakistan","India"]
secondList = ["USA","China"]
# firstList.append(secondList)
firstList.extend(secondList)
print(firstList)