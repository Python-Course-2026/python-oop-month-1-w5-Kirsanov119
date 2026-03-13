import json
import csv

csv_file = 'users.csv'
json_file = 'users.json'
data=[]
def csv_to_json(filename):
    with open(filename) as csvfile:
        csv_reader = csv.DictReader(filename)
        for row in csv_reader:
            data.append(row)
        with open(json_file, 'w') as jsonfile:
            json.dump(data, jsonfile)
csv_to_json('users.csv')