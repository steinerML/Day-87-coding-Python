import csv

filename = 'realestate.csv'

with open (filename, encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)

    for row in reader:
        print(row['city'], row['price'], row['sq__ft'])
    
    #Print all row by row
    # for row in reader:
    #     print(row)