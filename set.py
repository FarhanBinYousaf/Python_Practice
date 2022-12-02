    #Sets:: 
    #1. Python set is unordered 
    #2. Python set is unchangeable ===> which means we cannot change it's value once set is created ,but can remove items and add new items.
    #3. Duplicates not allowed in python set
    #4. Python set having no index 

# myset = {"Pakistan","India","China"}
# # print(len(myset))
# # print(type(myset))
# print(myset)


# mySet = {"Pakistan","India"}
# mySet.add("China")
# print(mySet)


# mySet = {"Pakistan","India","China"}
# mySet.remove("Pakistan")
# print(mySet)

mySet = {"Pakistan","India"}
mySet.discard("Pakistan")
print(mySet)