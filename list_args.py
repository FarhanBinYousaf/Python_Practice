
def mySum(*args):
    total = 0
    for num in args:
        total = total + num
    return total
myList = [1,2,3,4]   # Here we are passing list as argument, to do so write * before list
print(mySum(*myList))


# def x(*y):
#     multiply=0
#     for i in y:
#         multiply +=i
#     return multiply
# y=[1,2,2,3]
# print(x(y)) 