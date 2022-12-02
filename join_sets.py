first_set = {"Pakistan","India"}
second_set = {"China","USA"}

    # To join two sets we can use two methods 
        #1. By using union()
        #2. By using update()
#1. By using union()
# third_set = first_set.union(second_set)
# print(third_set)

#2. By using update() 
first_set.update(second_set)
print(first_set)



# Note : since sets are unordered so we cannot imagine which item will come to which place.