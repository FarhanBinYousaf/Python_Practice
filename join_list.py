    # 1. Join list using + operator
   
#  listOne = ["Pakistan","India","China"]
# listTwo = [1,2,3,4,5]
# listThree = listOne + listTwo
# print(listThree)

    #2. Join list using append() method to append all items from list two to list one
# listOne = ["Pakistan","India","China"]
# listTwo = [1,2,3,4,5]
# for x in listTwo:
#     listOne.append(x)
# print(listOne)

    #3. Join the list using extend() method
listOne = ["Pakistan","India","China"]
listTwo = [1,2,3,4,5]
listOne.extend(listTwo)
print(listOne)

