import json
import requests
import pandas as pd

root_url = r'https://swapi.dev/api/people/'

def get_data(url):
    try:
        response = requests.get(url)
        data = response.content.decode()
    except Exception as e:
        print("Could'nt reach the server")
        return None
    else:
        json_data = json.loads(data)
    return json_data

def get_top_ten_characters(json_data, max_characters=10):
    characters = json_data['results']
    characters.sort(key=lambda x:len(x['films']), reverse=True)
    
    df = pd.DataFrame(characters)
    df['height'] = pd.to_numeric(df['height'])
    df = df.sort_values(by=["height"],ascending=False) 

    species_type = []
    for x in df['species']:
        if x:
            x = list(x)[0] 
            print(x)
            sp_data = json.loads(requests.get(x).content.decode())#['name'])
            species_type.append(sp_data['name'])
        else:
            species_type.append('')
    print(species_type)

    appearances = [len(x) for x in df['films']]

    df['appearances'] = appearances
    df['species'] = species_type

    export_columns = ['name','species','height','appearances']

    df.to_csv(r'Exported.csv', index=False, header=False, columns=export_columns, sep=',', encoding='utf-8')
    return 0 

results = get_data(root_url)
found_characters = get_top_ten_characters(results)