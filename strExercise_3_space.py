#with space problem 
# name, chr = input("Enter Your Name separated with comma").split(",")
# lenght = len(name)
# print(f"Your name length is {lenght} and chracter in your name is {name.lower().count(chr.lower())} times ")
#without space problem 
# strip() =========> is used to remove space from name
# from operator import length_hint


name, chr = input("Enter Your name separated with comma").split(",")
length = len(name)
print(f"Your name length is {length} and character in your name is {name.strip().lower().count(chr.strip().lower())} times")

