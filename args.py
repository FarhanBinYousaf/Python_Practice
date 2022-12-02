 # With Normal Function 
# def total_fun(a,b):
#     return a + b
# print(total_fun(3,4))

#  With *args  ===> This function don't need to take multiple parameters
def total_fun(*args):
    total = 0
    for num in args:
        total = total + num
    return total
print(total_fun(1,2,3))  