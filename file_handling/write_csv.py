# from asyncore import write
from csv import writer
with open('write_file.csv','w',newline='') as f:
    csv_writer = writer(f)
    # 2 methods for writing in CSV files
    #1. 
    csv_writer.writerow(['name','country'])
    csv_writer.writerow(['Harry','India'])
    csv_writer.writerow(['Harshit','India'])
    #2.
    # csv_writer.writerows[['name','country'],['Harry','India'],['Harshit','India']]