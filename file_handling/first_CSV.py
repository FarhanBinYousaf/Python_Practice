from csv import reader

with open('first.csv','r') as f:
    csv_reader = reader(f)   # This is an iterator, so we just can iterate loop through iterator
    next(csv_reader)  # This will not show the heading of CSV file 
    for row in csv_reader:
        print(row)
