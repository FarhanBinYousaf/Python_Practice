# from unicodedata import name
name, chrt = input("Enter Your Name and char separated by comma").split(",")
length = len(name)
x = name.lower()
y = x.count(chrt)
print(f"Name lenght is {length} and the number {chrt} in your name is {y} times")