from csv import DictWriter
with open('final.csv', 'w', newline='') as f:
    csv_writer = DictWriter(f, fieldnames = ['firstname','lastname','age'])
    csv_writer.writeheader()
    # writerow
    #csv_writer.writerow({
    #    'firstname': 'Vivek',
    #    'lastname' : 'Vishan',
    #    'age' : 25 
    # })
    #csv_writer.writerow({
    #    'firstname': 'Vivek',
    #    'lastname' : 'Vishan',
    #    'age' : 25 
    #})

    # writerows
    csv_writer.writerows([
        {'firstname': 'Vivek', 'lastname' : 'Vishan', 'age' : 25},
        {'firstname': 'Aneel', 'lastname' : 'Vishan', 'age' : 25},
        {'firstname': 'Madan', 'lastname' : 'Vishan', 'age' : 25}
    ])