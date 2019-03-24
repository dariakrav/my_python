import csv

def dict_transport(file):
    list = dict()
    with open(file) as csv_file:
        text_reader = csv.DictReader(csv_file, delimiter = ',')
        for row in text_reader:
            print(row)

print(dict_transport('input.txt'))