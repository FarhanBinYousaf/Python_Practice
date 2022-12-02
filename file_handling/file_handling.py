# Read File 
# open() method =====> This is used if file exist.
# read() method
# close() method
# tell() method ===> Tells us the current position of cursor in file
# seek() method
# readline() method  ===> Read only one line at a time 


f = open("file.txt","r")  #====> This takes multiple parameters like r,a,w,x etc
# print(f"cursor position {f.tell()} ")
# print(f.read())
# print(f.readlin(),end="")
# # print(f.readline())
print(f.readlines())

# print(f"Before seek method {f.tell()} ")
# f.seek(0)
# print(f"After seek method:  {f.tell()} ")
f.close()
