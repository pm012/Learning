import csv

FILENAME = './module12_serialization/teory/users.csv'

users = [
  {'name': 'Roman', 'age': 22, 'sex': 'male'},
  {'name': 'Oksana', 'age': 22, 'sex': 'female'},
  {'name':'Mike', 'age': 22, 'sex': 'male'},
]

with open(FILENAME, 'w', newline='', encoding='utf-8') as file:
    columns = ['name', 'age', 'sex']
    writer = csv.DictWriter(file, delimiter=',', fieldnames=columns)
    writer.writeheader()
    for row in users:
        writer.writerow(row)

FILENAME1 = './module12_serialization/teory/names.csv'
import csv

with open(FILENAME1, 'w', newline='\n') as csvfile:
    field_names = ['first_name', 'last_name']
    writer = csv.DictWriter(csvfile, fieldnames=field_names)
    writer.writeheader()
    writer.writerow({'first_name': 'Baked', 'last_name': 'Banana'})
    writer.writerow({'first_name': 'Lovely', 'last_name': 'Octopus'})
    writer.writerow({'first_name': 'Sad', 'last_name': 'Novelist'})

with open(FILENAME1) as file:
  print(file.read())

# FileReader example
with open(FILENAME, 'r', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)

with open(FILENAME, 'r', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row.get('name'))