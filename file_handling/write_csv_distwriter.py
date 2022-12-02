from csv import DictWriter
# from csv import DictReader
with open('write_csv_dictwriter.csv','w',newline='') as f:
    csv_writer = DictWriter(f,fieldnames=['firstName','lastName','email'])
    csv_writer.writeheader()
    csv_writer.writerow({
        'firstName':'Harry',
        'lastName': 'Clari',
        'email':'harry@gmail.com'
    })
    csv_writer.writerow({
        'firstName':'shari',
        'lastName': 'Clari',
        'email':'harry@gmail.com'
    })
    csv_writer.writerow({
        'firstName':'Harshit',
        'lastName': 'Clari',
        'email':'harry@gmail.com'
    })
    csv_writer.writerow({
        'firstName':'Farhan',
        'lastName': 'Clari',
        'email':'harry@gmail.com'
    })
# with open('write_csv_dictwriter.csv','r') as r:
#     csv_reader = DictReader(r) 
#     for row in csv_reader:
#         print(row)