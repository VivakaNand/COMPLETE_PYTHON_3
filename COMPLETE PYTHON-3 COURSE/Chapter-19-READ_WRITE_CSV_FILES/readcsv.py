from csv import reader

with open('file.csv', 'r') as f:
    csv_reader = reader(f)
    # iterator
    next(csv_reader) # to hide the headers
    for row in csv_reader:
        print(row)