
# Here i'm going to write and read data into/from same CSV file, First i will write and then will read
from csv import DictWriter
from csv import DictReader
with open('read_write.csv','w',newline='') as f:
    csv_writer = DictWriter(f,fieldnames=['name','email','address'])
    csv_writer.writeheader()
    csv_writer.writerows([
        {'name':'Harry','email':'harry@gmail.com','address':'Sargodha'},
        {'name':'Clari','email':'clari@gmail.com','address':'India'},
        {'name':'harshit','email':'harshit@gmail.com','address':'India'}
    ])
# Below part is for displaying data from CSV file

with open('read_write.csv','r') as r:
    csv_reader = DictReader(r)
    for row in csv_reader:
        print(row)