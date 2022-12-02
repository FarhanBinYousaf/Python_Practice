def paperwork(n, m):
    if n < 0:
        print(0)
    elif m < 0:
        print(0)
    else:
        BlankPages = n * m 
        return BlankPages
pages = int(input())
classmates  = int(input())
print(paperwork(pages,classmates))




# print(type(newString))
