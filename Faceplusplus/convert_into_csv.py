import csv

# apro e parso il file .json
def convert(response, id):

    #creo e apro un file .csv per scrivere
    file_parsed = open('File_Parsered.csv', 'w')
    
    #creo il writer
    writer = csv.writer(file_parsed)

    #ciclo per tradurre il file .json in quello .csv
    header = ['user', 'age', 'gender', 'ethnicity']

    #creo il writer
    writer.writerow(header)

    #estrarre dal file json i valori di età, genere ed etnia
    age = response['outputs'][0]['data']['regions'][0]['data']['face']['age_appearance']['concepts'][0]['name']
    gender = response['outputs'][0]['data']['regions'][0]['data']['face']['gender_appearance']['concepts'][0]['name']
    ethnicity = response['outputs'][0]['data']['regions'][0]['data']['face']['multicultural_appearance']['concepts'][0]['name']
    writer.writerow([id, age, gender, ethnicity])

    #salvo e chiudo il file .csv
    file_parsed.close()
