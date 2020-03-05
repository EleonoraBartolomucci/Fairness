import json
import csv

# apro e parso il file .json
data = open(r'C:\Users\Mela\Desktop\test.txt').read()
data_parsed = json.loads(data)

# creo e apro un file .csv per scrivere
file_parsed = open('File_Parsered.csv', 'w')
# creo il writer
writer = csv.writer(file_parsed)

# ciclo per tradurre il file .json in quello .csv
header = ['gender', 'age', 'emotion', 'ethnicity']

writer.writerow(header)

# flatten_file = flatten_json(data_parsed)
# print(flatten_file)
for persona in data_parsed:
    for face in persona['faces']:
        for attribute in face['attributes'].keys():
            writer.writerow(attribute)
# writer.writerow([persona[h] for h in header])

# salvo e chiudo il file .csv
file_parsed.close()
