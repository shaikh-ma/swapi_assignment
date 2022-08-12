from urllib.request import urlopen
import json,csv

resp = urlopen(r'https://swapi.dev/api/people/')
data  = resp.read().decode()
print(resp.status)

json_data = json.loads(data)

characters = json_data['results']

characters.sort(key=lambda x: len(x['films']),reverse=True)

selected_characters = characters[:10]

selected_characters.sort(key=lambda x: len(x['height']),reverse=True)

species_type = []

for character in selected_characters:
    link = character['species']
    
    if link:
        link = link[0]
        sp_type = json.loads(urlopen(link).read().decode())
        species_type.append(sp_type['name'])
    else:
        species_type.append('')

appearances = [len(x['films']) for x in selected_characters]

for ind,character in enumerate(selected_characters):
    character['species_name'] = species_type[ind]
    character['appearances'] = appearances[ind]

with open('Exported.csv','w',newline="") as export:
    csv_writer = csv.writer(export)
    for row in selected_characters:
        line = [row['name'],row['species_name'],row['height'],row['appearances']]
        csv_writer.writerow(line)
