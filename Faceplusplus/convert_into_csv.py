import json
import csv

# apro e parso il file .json
data = open(path_to_my_file\file.txt').read()
data_parsed = json.loads(data)

# creo e apro un file .csv per scrivere
file_parsed = open('File_Parsered.csv', 'w')
# creo il writer
writer = csv.writer(file_parsed)

# ciclo per tradurre il file .json in quello .csv
header = ['gender', 'ethnicity']

#creo il writer            
writer.writerow(header)

#ciclo per estrarre dal file json i valori di genere ed etnia
for persona in data_parsed:
    for face in persona['faces']:
        writer.writerow([face['attributes']['gender']['value'],
                         face['attributes']['ethnicity']['value']])

# salvo e chiudo il file .csv
file_parsed.close()
