import csv
from pprint import pprint

# Example 1: get from the file dictionary {country_code:country_name}
FILENAME = './module12_serialization/teory/countries.csv'
country_codes = {}

with open(FILENAME) as file:
    reader = csv.reader(file)
    for line in reader:
        country_codes[line[0]] = line[1]
    country_codes.pop('Code')

print(country_codes['AD'])
print(country_codes.get('UA'))

# Example2: print the squeare power and cubic power for numbers
FILENAME1 = './module12_serialization/teory/table1.csv'
with open(FILENAME1, 'w', newline='') as file:
    writer = csv.writer(file)
    for i in range(1, 21):
        writer.writerow([i, pow(i, 2), pow(i, 3)])

with open(FILENAME1) as file:
    reader = csv.reader(file)
    result = []
    for line in reader:
        result.append(line)

print(result)
pprint(result)