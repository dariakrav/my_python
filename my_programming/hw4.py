import csv



def redact(file):

    with open(file, 'r') as i:
        reader = csv.DictReader(i, delimiter=',')
        for row in reader:
            print(row)

print(redact('input.csv'))

