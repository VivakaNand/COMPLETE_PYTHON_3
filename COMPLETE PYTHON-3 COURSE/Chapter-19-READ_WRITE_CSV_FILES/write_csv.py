# writer , DictWriter
from csv import writer
with open('file1.csv', 'w', newline='') as f:
    csv_writer = writer(f)
    # methods - writerow - writerows
    # writerow - use to write single row in file
    #csv_writer.writerow(['name','country'])
    #csv_writer.writerow(['Vivek','Pak'])
    #csv_writer.writerow(['Aneel','Pak'])

    # writerows - use to write multiple rows in file
    csv_writer.writerows([['name','country'],['Vivek','Pak'],['Aneel','Pak'],['Madan','Ind']])
