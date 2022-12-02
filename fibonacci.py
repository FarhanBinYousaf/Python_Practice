# from itertools import count


numb = int(input("How many time? "))
n1, n2 = 0, 1
count = 0
while count < numb:
    print(n1)
    nth = n1 + n2
    n1 = n2
    n2 = nth
    count = count + 1