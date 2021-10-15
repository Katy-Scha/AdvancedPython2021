import os
import json
import csv

os.chdir('vitamins') #vitamins in curr directory
files = os.listdir()
#texts = filter(lambda x: x.endswith('.txt'), files)
texts = [f for f in files if f.endswith('.txt')]

titles = ['vitamin', 'vitamers', 'solubility', 'daily_requirement', 'deficiency_diseases']

data_json = []
data_csv = [titles]
for filename in texts:
    with open(filename, "r") as file:
        current_vit = []
        current_vit.append(file.readline().strip())
        current_vit.append(file.readline().strip().split(', '))
        current_vit.append(file.readline().strip())
        current_vit.append(file.readline().strip())
        current_vit.append(file.readline().strip().split(', '))

        data_json.append(dict(zip(titles, current_vit)))
        data_csv.append(current_vit)

with open("vitamins.json", "w") as out:
    json.dump(data_json, out, indent=1)

with open("vitamins.csv", "w") as out:
    writer = csv.writer(out)
    for vit in data_csv:
        writer.writerow(vit)