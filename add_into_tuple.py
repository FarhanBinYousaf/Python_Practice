        # To add items to tuple 
    #1. First convert tuple into list, modify that list and then convert that list back to tuple
# myTuple = ("Pakistan","India","USA")
#     # Since Tuple is unchangeable so we cannot add or remove items to or from tuple
#     # so to do this first convert tuple into list, modify the list and then convert back to tuple
# newList = list(myTuple)
# newList.append("Afghanistan")
# newTuple = tuple(newList)
# print(newTuple)
# # print(myTuple)

    #2. Add tuple to a tuple (because tuple can b added to other tuple)

firtTuple = ("Harry","Shary")
secondTuple = ("Johen",)
thirdTuple = firtTuple + secondTuple
print(thirdTuple)