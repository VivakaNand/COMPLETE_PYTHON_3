from csv import DictReader
# ordered dict
with open('file.csv', 'r') as f:
    #csv_reader = DictReader(f)
    csv_reader = DictReader(f, delimiter = '|') # if seperated by different delimiters use this
    for row in csv_reader:
        #print(row)
        print(row['name']) # display name in dict