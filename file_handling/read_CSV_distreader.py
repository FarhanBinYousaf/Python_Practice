from csv import DictReader   # This is method of python which is used to read csv files 

with open('first.csv','r') as f:
    # csv_reader = DictReader(f,delimiter='|')
    csv_reader = DictReader(f)
    for row in csv_reader:
        print(row)
        # print(row['email'])